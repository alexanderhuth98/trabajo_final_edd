from collections import defaultdict, deque


class GrafoDiagnostico:
    def __init__(self):
        self.grafo = defaultdict(list)

    def agregar_paso(self, paso, dependencias=[]):
        """
        Agrega un paso al grafo, con sus dependencias opcionales.
        :param paso: Nombre del paso.
        :param dependencias: Lista de pasos de los que depende.
        """
        for dependencia in dependencias:
            self.grafo[dependencia].append(paso)
        if paso not in self.grafo:
            self.grafo[paso] = []  # Asegurarse de incluir el paso sin dependencias.

    def orden_topologico(self):
        """
        Realiza el ordenamiento topológico.
        :return: Lista ordenada de pasos.
        """
        # Calcular grados de entrada
        grado_entrada = {nodo: 0 for nodo in self.grafo}
        for dependencias in self.grafo.values():
            for nodo in dependencias:
                grado_entrada[nodo] += 1

        # Nodos con grado de entrada 0
        cola = deque([nodo for nodo, grado in grado_entrada.items() if grado == 0])
        orden = []

        while cola:
            actual = cola.popleft()
            orden.append(actual)

            for vecino in self.grafo[actual]:
                grado_entrada[vecino] -= 1
                if grado_entrada[vecino] == 0:
                    cola.append(vecino)

        # Verificar ciclos
        if len(orden) != len(self.grafo):
            raise ValueError("El grafo tiene ciclos, no se puede realizar el ordenamiento.")

        return orden


# Crear el grafo de diagnóstico
diagnostico = GrafoDiagnostico()

# Definir los pasos y sus dependencias
diagnostico.agregar_paso("Recolectar síntomas iniciales")
diagnostico.agregar_paso("Determinar posibles enfermedades", ["Recolectar síntomas iniciales"])
diagnostico.agregar_paso("Ordenar análisis de sangre", ["Determinar posibles enfermedades"])
diagnostico.agregar_paso("Ordenar radiografías", ["Determinar posibles enfermedades"])
diagnostico.agregar_paso("Revisar resultados de análisis de sangre", ["Ordenar análisis de sangre"])
diagnostico.agregar_paso("Revisar resultados de radiografías", ["Ordenar radiografías"])
diagnostico.agregar_paso("Confirmar diagnóstico", ["Revisar resultados de análisis de sangre", "Revisar resultados de radiografías"])
diagnostico.agregar_paso("Iniciar tratamiento", ["Confirmar diagnóstico"])

# Ordenamiento topológico
try:
    pasos_ordenados = diagnostico.orden_topologico()
    print("Secuencia de pasos para el diagnóstico:")
    for paso in pasos_ordenados:
        print(f"- {paso}")
except ValueError as e:
    print(f"Error: {e}")
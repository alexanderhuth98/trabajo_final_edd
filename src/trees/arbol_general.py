from Paciente import Paciente
from nodo_arbol_general import Nodo


class Arbol:
    """Clase que representa un árbol con una raíz."""
    def __init__(self, raiz: Nodo) -> None:
        """
        Inicializa un árbol con un nodo raíz.
        
        Args:
            raiz (Nodo): Nodo raíz del árbol.
        """
        self.raiz: Nodo = raiz

    def agregar_hijo_a_nodo(self, nodo_padre: Nodo, hijo: Nodo) -> None:
        """
        Agrega un nodo hijo a un nodo padre específico.
        
        Args:
            nodo_padre (Nodo): Nodo al que se le agregará el hijo.
            hijo (Nodo): Nodo hijo a agregar.
        """
        nodo_padre.agregar_hijo(hijo)

    def mostrar_arbol(self, nodo: Nodo = None, nivel: int = 0) -> None:
        """
        Muestra el árbol jerárquicamente desde un nodo.
        
        Args:
            nodo (Nodo, opcional): Nodo desde el que se inicia la visualización.
                                  Por defecto, se utiliza la raíz.
            nivel (int, opcional): Nivel de profundidad actual. Por defecto, 0.
        """
        if nodo is None:
            nodo = self.raiz
        print("  " * nivel + str(nodo.valor))
        for hijo in nodo.hijos:
            self.mostrar_arbol(hijo, nivel + 1)


# Ejemplo de uso
# Crear nodos y árbol para el paciente 1
paciente1 = Paciente('Juan', 'Perez', 30, 12345678, 1123456789, 
                     'Calle Falsa 123', 'Springfield', 'OSDE')
nodo_raiz1 = Nodo(paciente1.nombres_paciente)
nodo_visita1 = Nodo("Visita 1: 24-03-08")
nodo_visita2 = Nodo("Visita 2: 2023-06-20")

arbol1 = Arbol(nodo_raiz1)
arbol1.agregar_hijo_a_nodo(nodo_raiz1, nodo_visita1)
arbol1.agregar_hijo_a_nodo(nodo_raiz1, nodo_visita2)

# Agregar diagnósticos y tratamientos
nodo_diagnostico1 = Nodo("Diagnóstico: Gripe")
nodo_tratamiento1 = Nodo("Tratamiento: Tarifol cada 6 hs")
nodo_diagnostico2 = Nodo("Diagnóstico: Diarrea")
nodo_tratamiento2 = Nodo("Tratamiento: Ibuprofeno cada 6 hs")

arbol1.agregar_hijo_a_nodo(nodo_visita1, nodo_diagnostico1)
arbol1.agregar_hijo_a_nodo(nodo_visita1, nodo_tratamiento1)
arbol1.agregar_hijo_a_nodo(nodo_visita2, nodo_diagnostico2)
arbol1.agregar_hijo_a_nodo(nodo_visita2, nodo_tratamiento2)

# Mostrar árbol del paciente 1
arbol1.mostrar_arbol()

from .grafo import Grafo

class GrafoMetodos(Grafo):
    """
    Clase que contiene métodos adicionales para manejar la información del grafo.
    """

    def agregar_vertice(self, vertice: str) -> None:
        """Agrega un vértice al grafo si no existe."""
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def agregar_arista(self, vertice1: str, vertice2: str, peso: int = 1) -> None:
        """Agrega una arista entre dos vértices del grafo."""
        if vertice1 in self.grafo and vertice2 in self.grafo:
            self.grafo[vertice1].append((vertice2, peso))
            if not self.dirigido:
                self.grafo[vertice2].append((vertice1, peso))
        else:
            raise ValueError(
                f"Vértices {vertice1} y/o {vertice2} no existen en el grafo."
            )

    def mostrar_grafo(self) -> None:
        """Muestra el grafo en formato legible."""
        for vertice, aristas in self.grafo.items():
            conexiones = ", ".join([f"{destino} (peso: {peso})" for destino, peso in aristas])
            print(f"{vertice}: {conexiones}")

    def eliminar_vertice(self, vertice: str) -> None:
        """Elimina un vértice y todas las aristas asociadas."""
        if vertice in self.grafo:
            del self.grafo[vertice]
            for conexiones in self.grafo.values():
                conexiones[:] = [arista for arista in conexiones if arista[0] != vertice]
        else:
            raise ValueError(f"El vértice {vertice} no existe en el grafo.")

    def eliminar_arista(self, vertice1: str, vertice2: str) -> None:
        """Elimina una arista entre dos vértices."""
        if vertice1 in self.grafo and vertice2 in self.grafo:
            self.grafo[vertice1] = [
                arista for arista in self.grafo[vertice1] if arista[0] != vertice2
            ]
            if not self.dirigido:
                self.grafo[vertice2] = [
                    arista for arista in self.grafo[vertice2] if arista[0] != vertice1
                ]
        else:
            raise ValueError(f"Vértices {vertice1} y/o {vertice2} no existen en el grafo.")

    def estan_conectados(self, vertice1: str, vertice2: str) -> bool:
        """Verifica si existe una conexión entre dos vértices."""
        return any(destino == vertice2 for destino, _ in self.grafo.get(vertice1, []))

    def obtener_conexiones(self, vertice: str) -> list:
        """Devuelve las conexiones de un vértice."""
        if vertice in self.grafo:
            return self.grafo[vertice]
        raise ValueError(f"El vértice {vertice} no existe en el grafo.")

    def bfs(self, inicio: str, objetivo: str) -> list:
        """Realiza una búsqueda en anchura (BFS) desde un vértice de inicio."""
        from collections import deque
        if inicio not in self.grafo or objetivo not in self.grafo:
            raise ValueError(f"Vértices {inicio} y/o {objetivo} no existen.")
        visitados = set()
        cola = deque([(inicio, [inicio])])

        while cola:
            actual, camino = cola.popleft()
            if actual == objetivo:
                return camino
            for vecino, _ in self.grafo.get(actual, []):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append((vecino, camino + [vecino]))

        return []  # No se encontró un camino

    def dfs(self, inicio: str, objetivo: str, visitados=None, camino=None) -> list:
        """Realiza una búsqueda en profundidad (DFS) desde un vértice de inicio."""
        if visitados is None:
            visitados = set()
        if camino is None:
            camino = []
        visitados.add(inicio)
        camino.append(inicio)

        if inicio == objetivo:
            return camino

        for vecino, _ in self.grafo.get(inicio, []):
            if vecino not in visitados:
                resultado = self.dfs(vecino, objetivo, visitados, camino)
                if resultado:
                    return resultado

        camino.pop()  # Retroceso
        return []

    def dijkstra(self, inicio: str) -> dict:
        """Implementa el algoritmo de Dijkstra para encontrar caminos mínimos desde un vértice."""
        import heapq
        if inicio not in self.grafo:
            raise ValueError(f"El vértice {inicio} no existe en el grafo.")

        distancias = {vertice: float('inf') for vertice in self.grafo}
        distancias[inicio] = 0
        cola_prioridad = [(0, inicio)]

        while cola_prioridad:
            distancia_actual, actual = heapq.heappop(cola_prioridad)

            if distancia_actual > distancias[actual]:
                continue

            for vecino, peso in self.grafo[actual]:
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(cola_prioridad, (distancia, vecino))

        return distancias



# Ejemplo de uso
hospitales = Grafo(dirigido=False)
hospitales.agregar_vertice('Clinica Espora')
hospitales.agregar_vertice('Clinica Ima')
hospitales.agregar_vertice('Hospital Gandulfo')
hospitales.agregar_vertice('Hospital Lucio Melendez')
hospitales.agregar_vertice('Sanatorio Modelo Burzaco')

hospitales.agregar_arista('Clinica Espora', 'Clinica Ima', 42)
hospitales.agregar_arista('Clinica Espora', 'Hospital Gandulfo', 100)
hospitales.agregar_arista('Clinica Ima', 'Hospital Lucio Melendez', 51)
hospitales.agregar_arista('Hospital Gandulfo', 'Hospital Lucio Melendez', 83)
hospitales.agregar_arista('Hospital Lucio Melendez', 
                          'Sanatorio Modelo Burzaco', 10)

print("\nRed de hospitales:")
hospitales.mostrar_grafo()

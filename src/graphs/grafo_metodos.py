from .grafo import Grafo
from collections import deque
from trees.arbol_binario import ArbolBinarioBusqueda

def agregar_vertice(self, vertice):
        # Verificamos que el vértice no se encuentre dentro de los vértices del grafo
        if vertice not in self.grafo:
            # Inicializo la lista de adyacencias
            self.grafo[vertice] = []

def agregar_arista(self, vertice1, vertice2, peso=0):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            # Para el caso en el que quieran utilizar un grafo pesado
            self.grafo[vertice1].append([vertice2, peso])

            if not self.dirigido:
                # Para el caso en el que quieran utilizar un grafo no dirigido  
                self.grafo[vertice2].append([vertice1, peso])  # no dirigido
        else:
            print(f"Uno o ambos vértices {vertice1} o {vertice2} no existen.")

def mostrar_grafo(self):
        # Mostrar el grafo de forma más legible
        print("\nRed de hospitales:\n")
        for vertice, adyacentes in self.grafo.items():
            print(f"{vertice} tiene conexiones con:")
            for vecino in adyacentes:
                print(f"  -> {vecino[0]} (Distancia: {vecino[1]} km)")
            print()  # Añadir una línea en blanco entre los vértices para mayor claridad


# DFS recursivo
def dfs(grafo, inicio, visitados=None):
    if visitados is None:
        # Inicializamos un conjunto vacío
        visitados = set()
    
    visitados.add(inicio)
    print(inicio, end=" ")

    for vecino in grafo.grafo[inicio]:
        if vecino[0] not in visitados:
            dfs(grafo, vecino[0], visitados)
    print()


def bfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])

    
    while cola:
        vertice = cola.popleft()

        if vertice not in visitados:
            print(vertice, end=" ")
            visitados.add(vertice)

            for vecino in grafo.grafo[vertice]:
                if vecino[0] not in visitados:
                    cola.append(vecino[0])
    print()


grafo = Grafo(dirigido=False)

arbol = ArbolBinarioBusqueda()

def agregar_vertice_grafo():
    vertice = input('Ingresa hospital: ')
    grafo.agregar_vertice(vertice)    
        
def agregar_arista_grafo():
    grafo.mostrar_grafo()
    vertice1 = input('Ingresa un hospital existente: ')
    vertice2 = input('Ingresa otro hospital existente: ')
    distancia = input('Ingresa la distancia entre hospitales: ')
    grafo.agregar_arista(vertice1, vertice2, distancia)    

def ver_todo_grafo():
    print('Vamos a mostrarte la red de hospitales')
    grafo.mostrar_grafo()
    hospital = input('''Ingresa el hospital en que se encuentra para mostrar las rutas mas cercanas
hacia lo ancho y a lo profundo del mapa: ''')
    print('Recorrido en profundidad:')
    dfs(grafo, hospital)
    print('Recorrido hacia lo ancho:')
    bfs(grafo, hospital)
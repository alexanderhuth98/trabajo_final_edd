class Paciente:
    def __init__(self, dni, nombre, apellido, edad):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.historial_enfermedades = []
        self.medicamentos = []
    
    def agregar_dni(self, dni):
        self.dni = dni
        
    def agregar_nombre(self, nombre):
        self.nombre = nombre
    
    def agregar_apellido(self, apellido):
        self.apellido = apellido 
    
    def agregar_edad(self, edad):
        self.edad = edad
        
    def agregar_historial_enfermedades(self, historial_enfermedades):
        self.historial_enfermedades.append(historial_enfermedades)
        
   
    
    def buscar_en_historial(self, histo_enf, clave):
        if not histo_enf:
            return False
        else:
            if histo_enf[0] == clave:
                return clave
            else:
                return self.buscar_en_historial(histo_enf[1:], clave) 
        
    def __str__(self):
        return f'El nombre es: {self.nombre}\nEl apellido es: {self.apellido}\nEl numero de DNI es: {self.dni}\nHistorial de enfermedades: {self.historial_enfermedades}\n---------------\n'
    

class Nodo:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None
    
    # Método para insertar un nodo en el árbol
    def insertar(self, clave, valor):
        self.raiz = self._insertar_recursivo(self.raiz, clave, valor)
    
    def _insertar_recursivo(self, nodo, clave, valor):
        if nodo is None:
            return Nodo(clave, valor)
        
        if clave < nodo.clave:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, clave, valor)
        elif clave > nodo.clave:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, clave, valor)
        else:
            # Si la clave ya existe, actualiza el valor
            nodo.valor = valor
        
        return nodo
    
    # Método para buscar un nodo por su clave
    def buscar(self, clave):
        return self._buscar_recursivo(self.raiz, clave)
    
    def _buscar_recursivo(self, nodo, clave):
        if nodo is None or nodo.clave == clave:
            return nodo
        
        if clave < nodo.clave:
            return self._buscar_recursivo(nodo.izquierda, clave)
        
        return self._buscar_recursivo(nodo.derecha, clave)
    
    # Método para eliminar un nodo por su clave
    def eliminar(self, clave):
        self.raiz = self._eliminar_recursivo(self.raiz, clave)
    
    def _eliminar_recursivo(self, nodo, clave):
        if nodo is None:
            return nodo
        
        if clave < nodo.clave:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, clave)
        elif clave > nodo.clave:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, clave)
        else:
            # Nodo a eliminar encontrado
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            
            # Nodo con dos hijos: obtener el sucesor (el valor más pequeño en el subárbol derecho)
            nodo.clave, nodo.valor = self._min_value_node(nodo.derecha)
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, nodo.clave)
        
        return nodo
    
    def _min_value_node(self, nodo):
        current = nodo
        while current.izquierda is not None:
            current = current.izquierda
        return current.clave, current.valor
    

    # Método para imprimir el árbol (en orden)
    def imprimir_inorder(self):
        self._imprimir_inorder_recursivo(self.raiz)

    def _imprimir_inorder_recursivo(self, nodo):
        if nodo:
            self._imprimir_inorder_recursivo(nodo.izquierda)
            print(nodo.valor)  # Muestra el Paciente
            self._imprimir_inorder_recursivo(nodo.derecha)
            
# Implementación de grafo utilizando lista de adyacencias

from collections import deque

class Grafo:
    def __init__(self, dirigido=False):
        # Inicializo grafo como un diccionario vacío
        self.grafo = {}  
        self.dirigido = dirigido

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



def cargar_paciente():
    opcion = input('\nVamos a empezar a cargar: Presione cualquier tecla para continuar\nLa carga finaliza cuando pones jjj: ')
    while opcion != 'jjj':
        nombre = input('Ingresa nombre: ')
        apellido = input('Ingresa Apellido: ')
        dni = int(input('Ingresa DNI: '))
        edad = int(input('Ingresa edad: '))
        enfermedades = input('Ingresa historial de enfermedades: ')
        datos = Paciente(dni, nombre, apellido, edad)
        datos.agregar_historial_enfermedades(enfermedades)
        arbol.insertar(dni, datos)
        opcion = input('\nSeguimos cargando?: Presione cualquier tecla para continuar\nLa carga finaliza cuando pones jjj: ')
    return '\nLa carga finalizo'

def modificar_un_paciente():
    print('Vamos a modificar un paciente')
    eliminar_un_paciente()
    nombre = input('Ingresa nombre: ')
    apellido = input('Ingresa Apellido: ')
    dni = int(input('Ingresa DNI: '))
    edad = int(input('Ingresa edad: '))
    enfermedades = input('Ingresa historial de enfermedades: ')
    datos = Paciente(dni, nombre, apellido, edad)
    datos.agregar_historial_enfermedades(enfermedades)
    arbol.insertar(dni, datos)
    
    
    
    

def eliminar_un_paciente():
    print('Vamos a eliminar un paciente')
    clave = int(input('Ingresa el DNI del paciente: '))
    eliminar = arbol.buscar(clave)
    if eliminar is None:
        return f'DNI: {clave} de paciente no encontrado.'
    
    # Si la clave existe, eliminamos el paciente
    arbol.eliminar(clave)
    return f'DNI: {clave} de paciente eliminado exitosamente.'

def agregar_al_historial():
    clave = int(input('Ingresa el DNI del paciente: '))
    buscar = arbol.buscar(clave)
    if buscar is None:
        return f'DNI: {clave} de paciente no encontrado.'
    paciente_encontrado = buscar.valor
    agregar = input('Ingresa nuevo historial: ')
    paciente_encontrado.agregar_historial_enfermedades(agregar)
    print('Se cargo con exitosamente')
    
    
    
def agregegar_vertice_grafo():
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
        

menu="""
(1) Cargar pacientes
(2) Mostrar pacientes 
(3) Modificar paciente
(4) Eliminar paciente
(5) Agregar al historial
(6) Cargar hospital
(7) Cargar distancia entre hospitales
(8) Mostrar red hospitales para translado de urgencia
(9) Salir
"""

print (menu)
opcion= int(input("ingrese una opcion del menu:"))
while opcion != 9:
    
    if(opcion==1):
        print('Elegiste la opcion 1')
        cargar_paciente()
        
    elif(opcion==2):
        print('Elegiste la opcion 2')
        arbol.imprimir_inorder()
    
    elif(opcion==3):
        print('Elegiste la opcion 3')
        modificar_un_paciente()
        
    elif(opcion==4):
        print('Elegiste la opcion 4')
        eliminar_un_paciente()
    
    elif(opcion==5):
        print('Elegiste la opcion 5')
        agregar_al_historial()
        
    
    elif(opcion==6):
        print('Elegiste la opcion 6')
        agregegar_vertice_grafo()
        f'Hospitales cargados: {grafo.mostrar_grafo()}'
        
    elif(opcion==7):
        print('Elegiste la opcion 7')
        agregar_arista_grafo()
        
    elif(opcion==8):
        print('Elegiste la opcion 8')
        ver_todo_grafo()
        
    
    else:
        print('No elegiste una opcion valida')
    
    print(menu)
    opcion = int(input('ingrese una opcion del menu:'))
        
	

	
print ("Gracias por usar el Sistema")
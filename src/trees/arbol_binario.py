from .nodo_arbol_binario import Nodo

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
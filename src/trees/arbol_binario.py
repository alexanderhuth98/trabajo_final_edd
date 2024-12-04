from Paciente import Paciente
from nodo_arbol_binario import Nodo
from cola_prioridad import ColaPrioridad



class ArbolBinarioBusqueda:
    """
    Clase que implementa un árbol binario de búsqueda para gestionar pacientes.

    Atributos:
        raiz (Nodo): Nodo raíz del árbol.
    """

    def __init__(self):
        """
        Inicializa un árbol binario de búsqueda vacío.
        """
        self.raiz = None

    def insertar(self, valor: Paciente):
        """
        Inserta un objeto Paciente en el árbol binario de búsqueda.

        Args:
            valor (Paciente): Paciente a insertar en el árbol.
        """
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor: Paciente):
        """
        Inserta un Paciente de forma recursiva en el árbol.

        Args:
            nodo (Nodo): Nodo actual en el que se evalúa la inserción.
            valor (Paciente): Paciente a insertar en el árbol.
        """
        if valor.dni < nodo.valor.dni:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        elif valor.dni > nodo.valor.dni:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def buscar(self, dni: int):
        """
        Busca un Paciente por su DNI en el árbol binario.

        Args:
            dni (int): DNI del paciente a buscar.

        Returns:
            Paciente: Paciente encontrado, o mensaje indicando que no existe.
        """
        paciente = self._buscar_recursivo(self.raiz, dni)
        if paciente is None:
            return 'Paciente no encontrado'
        return paciente

    def _buscar_recursivo(self, nodo, dni: int):
        """
        Realiza la búsqueda de un Paciente de forma recursiva.

        Args:
            nodo (Nodo): Nodo actual donde se realiza la búsqueda.
            dni (int): DNI del paciente a buscar.

        Returns:
            Paciente: Paciente encontrado o None si no existe.
        """
        if nodo is None or nodo.valor.dni == dni:
            return nodo.valor if nodo else None
        if dni < nodo.valor.dni:
            return self._buscar_recursivo(nodo.izquierda, dni)
        return self._buscar_recursivo(nodo.derecha, dni)

    def eliminar(self, dni: int):
        """
        Elimina un Paciente del árbol por su DNI.

        Args:
            dni (int): DNI del paciente a eliminar.
        """
        self.raiz = self._eliminar_recursivo(self.raiz, dni)

    def _eliminar_recursivo(self, nodo, dni: int):
        """
        Elimina un Paciente de forma recursiva.

        Args:
            nodo (Nodo): Nodo actual donde se realiza la eliminación.
            dni (int): DNI del paciente a eliminar.

        Returns:
            Nodo: Nodo actualizado tras la eliminación.
        """
        if nodo is None:
            return nodo

        if dni < nodo.valor.dni:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, dni)
        elif dni > nodo.valor.dni:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, dni)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda

            # Nodo con dos hijos
            nodo.valor = self._minimo(nodo.derecha)
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, nodo.valor.dni)

        return nodo

    def _minimo(self, nodo):
        """
        Encuentra el nodo con el valor mínimo en el subárbol.

        Args:
            nodo (Nodo): Nodo raíz del subárbol.

        Returns:
            Paciente: Paciente con el valor mínimo.
        """
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo.valor

    def imprimir_inorder(self):
        """
        Imprime el contenido del árbol en orden ascendente.
        """
        self._imprimir_inorder_recursivo(self.raiz)

    def _imprimir_inorder_recursivo(self, nodo):
        """
        Recorre e imprime el árbol en orden de forma recursiva.

        Args:
            nodo (Nodo): Nodo actual del recorrido.
        """
        if nodo:
            self._imprimir_inorder_recursivo(nodo.izquierda)
            print(nodo.valor)
            self._imprimir_inorder_recursivo(nodo.derecha)

    def mostrar_historial(self, dni):
        """
        Muestra el historial médico de un paciente por su DNI.

        Args:
            dni (int): DNI del paciente.
        """
        paciente = self.buscar(dni)
        if paciente != 'Paciente no encontrado':
            print(paciente.mostrar_historial_paciente())
        else:
            print("Paciente no encontrado.")

    def agregar_enfermedad(self, dni, enfermedad, medicina):
        """
        Agrega una enfermedad al historial de un paciente.

        Args:
            dni (int): DNI del paciente.
            enfermedad (str): Nombre de la enfermedad.
            medicina (str): Medicamento para la enfermedad.
        """
        paciente = self.buscar(dni)
        if paciente != 'Paciente no encontrado':
            print(paciente.agregar_enfermedad(enfermedad, medicina))
        else:
            print("Paciente no encontrado.")

    def listar_por_localidad(self, localidad):
        """
        Lista los pacientes que residen en una localidad específica.

        Args:
            localidad (str): Localidad a buscar.
        """
        pacientes = []
        self._listar_por_localidad_recursivo(self.raiz, localidad, pacientes)
        if pacientes:
            for paciente in pacientes:
                print(paciente)
        else:
            print(f"No se encontraron pacientes en la localidad '{localidad}'.")

    def _listar_por_localidad_recursivo(self, nodo, localidad, pacientes):
        """
        Lista pacientes por localidad de forma recursiva.

        Args:
            nodo (Nodo): Nodo actual del árbol.
            localidad (str): Localidad a buscar.
            pacientes (list): Lista de pacientes encontrados.
        """
        if nodo:
            if nodo.valor.localidad_paciente.lower() == localidad.lower():
                pacientes.append(nodo.valor)
            self._listar_por_localidad_recursivo(nodo.izquierda, localidad, pacientes)
            self._listar_por_localidad_recursivo(nodo.derecha, localidad, pacientes)




# Ejemplo de uso
paciente1 = Paciente("Juan", "Pérez", 30, 12345678, "123456789", "Calle Falsa 123", "Buenos Aires", "OSDE" , 5)
paciente2 = Paciente("Ana", "García", 25, 87654321, "987654321", "Calle Real 456", "Córdoba", "Swiss Medical" , 1)
paciente3 = Paciente("Carlos", "Sánchez", 40, 56789012, "456789123", "Avenida Siempreviva 789", "Mendoza", "Galeno" , 3)

arbol = ArbolBinarioBusqueda()
arbol.insertar(paciente1)
arbol.insertar(paciente2)
arbol.insertar(paciente3)

print("Árbol in-order:")
arbol.imprimir_inorder()

print("\nHistorial de un paciente:")
arbol.mostrar_historial(12345678)

print("\nAgregando enfermedad:")
arbol.agregar_enfermedad(12345678, "Diabetes", "Insulina")

print("\nListar pacientes en Córdoba:")
arbol.listar_por_localidad("Córdoba")

# Crear algunos pacientes con diferentes niveles de prioridad
paciente1 = Paciente("Juan", "Pérez", 30, 12345678, "123456789", "Calle Falsa 123", "Buenos Aires", "OSDE", prioridad=2)  # Urgente
paciente2 = Paciente("Ana", "García", 25, 87654321, "987654321", "Calle Real 456", "Córdoba", "Swiss Medical", prioridad=4)
paciente3 = Paciente("Carlos", "Sánchez", 40, 56789012, "456789123", "Avenida Siempreviva 789", "Mendoza", "Galeno", prioridad=1)  # Muy urgente

# Crear cola de prioridades
cola = ColaPrioridad()
cola.insertar(paciente1)
cola.insertar(paciente2)
cola.insertar(paciente3)

# Mostrar los pacientes en la cola por prioridad (de mayor urgencia a menor)
print("Pacientes por orden de prioridad:")
cola.mostrar()

# Extraer pacientes en orden de urgencia
print("\nAtendiendo pacientes en orden de urgencia:")
while not cola.esta_vacia():
    paciente_atendido = cola.extraer()
    print(f"Atendiendo a: {paciente_atendido}")
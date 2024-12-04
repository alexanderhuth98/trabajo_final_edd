

class Nodo:
    """
    Clase que representa un nodo de un árbol binario.

    Atributos:
        valor (Paciente): Objeto de tipo Paciente almacenado en el nodo.
        izquierda (Nodo): Referencia al hijo izquierdo.
        derecha (Nodo): Referencia al hijo derecho.
    """

    def __init__(self, valor):
        """
        Inicializa un nodo del árbol binario.

        Args:
            valor (Paciente): Objeto de tipo Paciente que se almacena en el nodo.
        """
        self.valor = valor
        self.izquierda = None
        self.derecha = None


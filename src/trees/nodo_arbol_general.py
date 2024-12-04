

class Nodo:
    """Clase que representa un nodo en un árbol."""
    def __init__(self, valor: str) -> None:
        """
        Inicializa un nodo con un valor y una lista de hijos vacía.
        
        Args:
            valor (str): El valor que almacena el nodo.
        """
        self.valor: str = valor
        self.hijos: list[Nodo] = []

    def agregar_hijo(self, hijo: 'Nodo') -> None:
        """
        Agrega un nodo hijo al nodo actual.
        
        Args:
            hijo (Nodo): Nodo a agregar como hijo.
        """
        self.hijos.append(hijo)

    def __repr__(self) -> str:
        return f"Nodo({self.valor})"
    
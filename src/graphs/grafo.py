class Grafo:
    """Clase que representa un grafo con soporte para grafos dirigidos."""
    def __init__(self, dirigido: bool = False) -> None:
        """
        Inicializa un grafo vacío.
        
        Args:
            dirigido (bool, opcional): Indica si el grafo es dirigido. 
                                       Por defecto, False.
        """
        self.grafo: dict[str, list[tuple[str, int]]] = {}
        self.dirigido: bool = dirigido


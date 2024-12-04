class Grafo:
    def __init__(self, dirigido=False):
        # Inicializo grafo como un diccionario vacío
        self.grafo = {}  
        self.dirigido = dirigido
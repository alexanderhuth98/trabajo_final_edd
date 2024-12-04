import heapq
from paciente import Paciente

class ColaPrioridad:
    """
    Clase que implementa una cola de prioridad para gestionar pacientes.

    Atributos:
        cola (list): Lista de pacientes organizada por prioridad.
    """

    def __init__(self):
        """
        Inicializa una cola de prioridad vacía.
        """
        self.cola = []

    def insertar(self, paciente: Paciente):
        """
        Inserta un paciente en la cola de prioridad.

        Args:
            paciente (Paciente): Paciente a insertar.
        """
        heapq.heappush(self.cola, (paciente.prioridad, paciente))

    def extraer(self):
        """
        Extrae el paciente con mayor prioridad.

        Returns:
            Paciente: Paciente extraído, o None si la cola está vacía.
        """
        if self.cola:
            _, paciente = heapq.heappop(self.cola)
            return paciente
        return None

    def esta_vacia(self):
        """
        Verifica si la cola está vacía.

        Returns:
            bool: True si la cola está vacía, False en caso contrario.
        """
        return len(self.cola) == 0

    def mostrar(self):
        """
        Muestra todos los pacientes en la cola, ordenados por prioridad.
        """
        for _, paciente in self.cola:
            print(paciente)
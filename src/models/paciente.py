import datetime
import pyzt


class Paciente:
    """
    Clase que representa a un paciente en el sistema.

    Atributos:
        nombres_paciente (str): Nombres del paciente.
        apellidos_paciente (str): Apellidos del paciente.
        edad (int): Edad del paciente.
        dni (int): Documento Nacional de Identidad del paciente.
        telefono_paciente (str): Teléfono del paciente.
        domicilio_paciente (str): Domicilio del paciente.
        localidad_paciente (str): Localidad del paciente.
        prepaga (str): Obra social o prepaga del paciente.
        prioridad (int): Nivel de urgencia del paciente.
        fecha_alta (str): Fecha y hora en que el paciente fue ingresado al sistema.
        historial_paciente (dict): Registro de enfermedades y medicinas del paciente.
        alergias (list): Lista de alergias del paciente.
    """

    def __init__(
        self, nombres_paciente, apellidos_paciente, edad, dni,
        telefono_paciente, domicilio_paciente, localidad_paciente,
        prepaga, prioridad
    ):
        """
        Inicializa una instancia de la clase Paciente.

        Args:
            nombres_paciente (str): Nombres del paciente.
            apellidos_paciente (str): Apellidos del paciente.
            edad (int): Edad del paciente.
            dni (int): Documento Nacional de Identidad.
            telefono_paciente (str): Teléfono de contacto.
            domicilio_paciente (str): Dirección del paciente.
            localidad_paciente (str): Localidad de residencia.
            prepaga (str): Obra social o prepaga del paciente.
            prioridad (int): Nivel de urgencia asignado.
        """
        self.nombres_paciente = nombres_paciente
        self.apellidos_paciente = apellidos_paciente
        self.edad = edad
        self.dni = dni
        self.telefono_paciente = telefono_paciente
        self.domicilio_paciente = domicilio_paciente
        self.localidad_paciente = localidad_paciente
        self.prepaga = prepaga
        self.fecha_alta = datetime.datetime.now(
            pyzt.timezone('America/Argentina/Buenos_Aires')
        ).strftime('%d/%m/%Y %H:%M:%S')
        self.historial_paciente = {}
        self.alergias = []
        self.prioridad = prioridad

    
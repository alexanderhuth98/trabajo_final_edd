class Paciente:
    def __init__(self, dni, nombre, apellido, edad):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.historial_enfermedades = []
        self.medicamentos = []

    def agregar_historial_enfermedades(self, enfermedad):
        self.historial_enfermedades.append(enfermedad)
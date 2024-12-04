from .paciente import Paciente
from trees.arbol_binario import ArbolBinarioBusqueda

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
        return historial_enfermedades
        
   
    
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


arbol = ArbolBinarioBusqueda()


def cargar_paciente():
    opcion = input('\nVamos a empezar a cargar: Presione cualquier tecla para continuar\nLa carga finaliza cuando pones jjj: ')
    while opcion != 'jjj':
        nombre = input('Ingresa nombre: ')
        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
            return 
        apellido = input('Ingresa Apellido: ')
        if apellido == "":
            print("Error: el apellido no puede estar vacío.")
            return 
        dni = int(input('Ingresa DNI: '))
        if dni == "":
            print("Error: el nombre no puede estar vacío.")
            return
        edad = int(input('Ingresa edad: '))
        if edad == "":
            print("Error: edad no puede estar vacío.")
            return 
        enfermedades = input('Ingresa historial de enfermedades: ')
        if enfermedades == "":
            print("Error: enfermedades no puede estar vacío.")
            return 
        datos = Paciente(dni, nombre, apellido, edad,)
        datos.agregar_historial_enfermedades(enfermedades)
        arbol.insertar(dni, datos )
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
    ArbolBinarioBusqueda().insertar(dni, datos)
    
    

def eliminar_un_paciente():
    print('Vamos a eliminar un paciente')
    clave = int(input('Ingresa el DNI del paciente: '))
    eliminar = ArbolBinarioBusqueda().buscar(clave)
    if eliminar is None:
        return f'DNI: {clave} de paciente no encontrado.'
    
    # Si la clave existe, eliminamos el paciente
    ArbolBinarioBusqueda().eliminar(clave)
    return f'DNI: {clave} de paciente eliminado exitosamente.'

def agregar_al_historial():
    clave = int(input('Ingresa el DNI del paciente: '))
    buscar = ArbolBinarioBusqueda().buscar(clave)
    if buscar is None:
        return f'DNI: {clave} de paciente no encontrado.'
    paciente_encontrado = buscar.valor
    agregar = input('Ingresa nuevo historial: ')
    paciente_encontrado.agregar_historial_enfermedades(agregar)
    print('Se cargo con exitosamente')
    

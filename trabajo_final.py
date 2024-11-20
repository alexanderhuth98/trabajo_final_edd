import datetime
import pytz

class Paciente:
    """
    Representa a un paciente en el sistema de gestión de historial médico.
    Atributos:
    Nombres_paciente(str): Nombre o nombres del/la paciente.
    Apellido_paciente(str): Apellido o apellidos del/la paciente.
    Edad(int): Años de edad del/la paciente.
    Dni(int): Documento nacional de identidad (dni) del/la paciente.
    Prepaga(str): Obra social / prepaga del/la paciente.
    Fecha_de_alta(str): Dia , mes , año y hora , minutos y segundos en el cual se dio de alta al paciente . Se importo la libreria Datetime para capturar los valores y Pytz para ajustar los valores a Buenos Aires.
    Historial_enfermedades(list): Lista de enfermedades que tuvo el/la paciente.
    Medicamentos_administrados(list): Lista de medicamentos que fueron administrados a el/la paciente.
    Alergias(list): Lista de alergias detectadas a el/la paciente. 
    Ejemplos de uso:
    print(paciente1.mostrar_nombres())
    print(paciente1.mostrar_apellidos())
    print(paciente1.mostrar_edad())
    print(paciente1.mostrar_dni())
    print(paciente1.mostrar_telefono())
    print(paciente1.mostrar_direccion())
    print(paciente1.mostrar_localidad())
    print(paciente1.mostrar_fecha_alta())
    print(paciente1.mostrar_historial_enfermedades())
    print(paciente1.mostrar_medicamentos_administrados())
    print(paciente1.mostrar_alergias())
    paciente1.actualizar_nombres('marina ines')
    paciente1.actualizar_apellidos('carretero lorenzo')
    paciente1.actualizar_edad(31)
    paciente1.actualizar_dni(38923741)
    paciente1.actualizar_telefono(1148237381)
    paciente1.actualizar_domicilio('santa maria de oro 211')
    paciente1.actualizar_localidad('temperley')
    paciente1.actualizar_prepaga('swiss medical')
    paciente1.agregar_enfermedad('diarrea')
    paciente1.agregar_enfermedad('gripe')
    paciente1.eliminar_enfermedad('diarrea')
    paciente1.agregar_medicamento_administrado('ibuprofeno')
    paciente1.agregar_medicamento_administrado('tafirol')
    paciente1.eliminar_medicamento_administrado('ibuprofeno')

    """
    def __init__(self , nombres_paciente , apellidos_paciente , edad , dni , telefono_paciente , domicilio_paciente , localidad_paciente , prepaga ):
        self.nombres_paciente = nombres_paciente
        self.apellidos_paciente = apellidos_paciente
        self.edad = edad
        self.dni = dni
        self.telefono_paciente = telefono_paciente
        self.domicilio_paciente = domicilio_paciente
        self.localidad_paciente = localidad_paciente
        self.prepaga = prepaga
        self.fecha_alta = datetime.datetime.now(pytz.timezone('America/Argentina/Buenos_Aires')).strftime('%d/%m/%Y %H:%M:%S')
        self.historial_enfermedades = []
        self.medicamentos_administrados = []
        self.alergias = []


    def __str__(self):
        """
        Devuelve una representación en forma de cadena del/la paciente.
        La representación incluye el nombre completo, edad, y prepaga del/la paciente.
        Está diseñada para ser legible y proporcionar una vista general de los datos
        más importantes del paciente.
        Returns:
        str: Una cadena que describe al paciente, incluyendo nombre completo, edad y prepaga.
        """
        return f'''nombre/s: {self.nombres_paciente}\n 
        apellido/s: {self.apellidos_paciente}\n
        edad : {self.edad}\n
        dni : {self.dni}\n
        telefono : {self.telefono_paciente}\n
        domicilio paciente : {self.domicilio_paciente}\n
        localidad paciente : {self.localidad_paciente}\n
        prepaga: {self.prepaga.title()}\n
        fecha de alta: {self.fecha_alta}\n
        historial de enfermedades :\n
        {self.historial_enfermedades}\n
        medicamentos administrados:\n
        {self.medicamentos_administrados}\n
        alergias:\n
        {self.alergias}\n
        '''


    def mostrar_nombres(self):
        """
        Devuelve una representacion en forma de cadena del nombre o nombres de el/la paciente.
        Returns:
        srt: Una cadena del nombre o nombres de el/la paciente.
        """
        return f'Nombre/s paciente: {self.nombres_paciente.title()}.'

    def mostrar_apellidos(self):
        """
        Devuelve una representacion en forma de cadena del apellido o apellidos de el/la paciente.
        Returns:
        srt: Una cadena del apellido o apellidos de el/la paciente.
        """
        return f'Apellido/s paciente: {self.apellidos_paciente.upper()}.'
    
    def mostrar_edad(self):
        """
        Devuelve una representacion en forma de cadena de la edad de el/la paciente.
        Returns:
        srt: Una cadena con la edad de el/la paciente.
        """
        return f'Edad: {self.edad} años.'

    def mostrar_dni(self):
        """
        Devuelve una representacion en forma de cadena del DNI de el/la paciente.
        Returns:
        srt: Una cadena con el DNI de el/la paciente.
        """
        return f'DNI paciente : {self.dni}.'

    def mostrar_telefono(self):
        """
        Devuelve una representacion en forma de cadena del telefono de el/la paciente.
        Returns:
        srt: Una cadena del telefono de el/la paciente.
        """
        return f'Telefono paciente: {self.telefono_paciente}.'
    def mostrar_domicilio(self):
        """
        Devuelve una representacion en forma de cadena del domicilio de el/la paciente.
        Returns:
        srt: Una cadena del domicilio donde recide de el/la paciente.
        """
        return f'Domicilio paciente: {self.domicilio_paciente.title()}.'

    def mostrar_localidad(self):
        """
        Devuelve una representacion en forma de cadena la localidad de el/la paciente.
        Returns:
        srt: Una cadena de la localidad donde recide el/la paciente.
        """
        return f'Localidad paciente: {self.localidad_paciente.title()}.'
    
    def mostrar_prepaga(self):
        """
        Devuelve una representacion en forma de cadena la prepaga u obra social de el/la paciente.
        Returns:
        srt: Una cadena del la prepaga/obra social de el/la paciente.
        """
        return f'Prepaga/obra social : {self.prepaga.title()}.'
    
    def mostrar_fecha_alta(self):
        """
        Devuelve una representacion en forma de cadena de la fecha de alta de el/la paciente.
        Returns:
        srt: Una cadena de la hora y fecha de alta de el/la paciente formateada en horas , minutos , segundos y dia , mes , año.
        """
        return f'Ingreso al sistema en la fecha {self.fecha_alta}.'
    
    def mostrar_historial_enfermedades(self):
        """
        Devuelve el historial de enfermedades del paciente en forma de cadena.

        Este método genera una representación en forma de texto del historial
        de enfermedades almacenado en el atributo `historial_enfermedades`.
        Inicialmente, el historial es una lista vacía, pero puede contener 
        nombres de enfermedades en formato de cadena.

        Returns:
        str: Una cadena que incluye el título "Historial de enfermedades"
        seguido por la lista de enfermedades registradas.
        """
        return f'Historial de enfermedades:\n{self.historial_enfermedades}'
    
    def mostrar_medicamentos_administrados(self):
        """
        Devuelve el historial de medicamentos administrados de el/la paciente en forma de cadena.

        Este método genera una representación en forma de texto del historial
        de medicamentos administrados almacenado en el atributo `medicamentos_administrados`.
        Inicialmente, el historial es una lista vacía, pero puede contener 
        nombres de medicamentos administrados en formato de cadena.

        Returns:
        str: Una cadena que incluye el título "Medicamentos administrados"
        seguido por la lista de medicamentos administrados.
        """
        return f'Medicamentos administrados:\n{self.medicamentos_administrados}'
    
    def mostrar_alergias(self):
        """
        Devuelve el historial de alergias de el/la paciente en forma de cadena.

        Este método genera una representación en forma de texto del historial
        de alergias almacenado en el atributo `alergias`.
        Inicialmente, el historial es una lista vacía, pero puede contener 
        nombres de alergias en formato de cadena.

        Returns:
        str: Una cadena que incluye el título "Alergias"
        seguido por la lista de alergias registradas.
        """
        return f'Alergias informadas:\n{self.alergias}'
    

# setters
# manejos de errores , algoritmos y programacion 1 ,pag 163


    def actualizar_nombres(self, nombres_paciente):
        if nombres_paciente == "":
            return "Error: el nombre no puede estar vacío."
        elif nombres_paciente == self.nombres_paciente:
            return "Error: el nombre ingresado es idéntico al actual."
        else:
            self.nombres_paciente = nombres_paciente
            return f"Nombre actualizado a: {self.nombres_paciente.title}"


    def actualizar_apellidos(self,apellidos_paciente):
        if apellidos_paciente == "":
            return "Error: el apellido no puede estar vacio."
        elif apellidos_paciente == self.apellidos_paciente:
            return "Error:el apellido ingresado es identico al actual."
        else:
            self.apellidos_paciente = apellidos_paciente
            return f'Apellido actualizado : {self.apellidos_paciente.upper()}'

    
    def actualizar_edad(self,edad):
        if edad == "":
            return "Error: edad no puede estar vacio."
        elif type(edad) is not int:
            raise TypeError('edad debe ser caracteres numericos')
        elif edad == self.edad:
            return "Error:edad ingresada es identica al actual."
        elif edad <0 and edad >110 :
            return 'edad no valida , ingrese una edad entre 0 y 110'
        else:
            self.edad = edad
            return f'edad actualizado : {edad}'


    def actualizar_dni(self,dni):
        if dni == "":
            return "Error: el campo DNI no puede estar vacio."
        elif type(dni) is not int:
            raise TypeError('dni debe ser caracteres numericos')
        elif dni == self.dni:
            return "Error:dni ingresado es identico al actual."
        elif dni <0 and dni >100000000 :
            return 'dni no valido , ingrese una dni entre 0 y 100000000 sin puntos ni espacios'
        else:
            self.dni = dni
            return f'edad actualizado : {self.edad}'

    def actualizar_telefono(self,telefono_paciente):
        if telefono_paciente == "":
            return "Error: el campo DNI no puede estar vacio."
        elif type(telefono_paciente) is not int:
            raise TypeError('telefono debe ser caracteres numericos')
        elif telefono_paciente == self.telefono_paciente:
            return "Error:telefono ingresado es identico al actual."
        elif len(str(telefono_paciente)) <9 and len(str(telefono_paciente)) >14 :
            return 'telefono no valido , ingrese un telefono entre 8 y 13 digitos sin puntos ni espacios'
        else:
            self.telefono_paciente = telefono_paciente
            return f'telefono actualizado : {self.telefono_paciente}'

    def actualizar_domicilio(self, domicilio_paciente):
        if domicilio_paciente == "":
            return "Error: el domicilio no puede estar vacío."
        elif domicilio_paciente == self.domicilio_paciente:
            return "Error: el domicilio ingresado es idéntico al actual."
        else:
            self.domicilio_paciente = domicilio_paciente
            return f"Domicilio actualizado a: {self.domicilio_paciente.title}"

    def actualizar_localidad(self, localidad_paciente):
        if localidad_paciente == "":
            return "Error: Localidad no puede estar vacío."
        elif localidad_paciente == self.localidad_paciente:
            return "Error: el domicilio ingresado es idéntico al actual."
        else:
            self.localidad_paciente = localidad_paciente
            return f"Localidad actualizado a: {self.localidad_paciente.title}"


    def actualizar_prepaga(self, prepaga):
        if prepaga == "":
            return "Error: prepaga no puede estar vacío."
        elif prepaga == self.prepaga:
            return "Error: el nombre ingresado es idéntico al actual."
        else:
            self.prepaga = prepaga
            return f"Prepaga actualizado a: {self.prepaga.title()}"

    def agregar_enfermedad (self,enfermedad):
        self.historial_enfermedades.append(enfermedad)

    def eliminar_enfermedad(self, enfermedad):
        if not self.historial_enfermedades:
            return 'No existen enfermedades registradas'
        else:
            if enfermedad in self.historial_enfermedades:
                self.historial_enfermedades.remove(enfermedad)
                return f'La enfermedad "{enfermedad}" ha sido eliminada.'
            else:
                return f'La enfermedad "{enfermedad}" no se encuentra en el registro.'

    def agregar_medicamento_administrado (self,medicamento_administrado):
        self.medicamentos_administrados.append(medicamento_administrado)

    def eliminar_medicamento_administrado(self, medicamento_administrado):
        if not self.medicamentos_administrados:
            return 'No existen enfermedades registradas'
        else:
            if medicamento_administrado in self.medicamentos_administrados:
                self.medicamentos_administrados.remove(medicamento_administrado)
                return f'el medicamento_administrado "{medicamento_administrado}" ha sido eliminado.'
            else:
                return f'el medicamento_administrado "{medicamento_administrado}" no se encuentra en el registro.'



# invocaciones
# parametros : nombre/s , apellido/s , edad , dni , telefono , domicilio , localidad ,prepaga   
paciente1 = Paciente('alexander german', 'Huth Simoni' , 26 , 41027676 , 2224544867 , 'paseo de la delicia 1105' , 'adrogue' , 'Sami salud')


print(paciente1.mostrar_nombres())
print(paciente1.mostrar_apellidos())
print(paciente1.mostrar_edad())
print(paciente1.mostrar_dni())
print(paciente1.mostrar_telefono())
print(paciente1.mostrar_domicilio())
print(paciente1.mostrar_localidad())
print(paciente1.mostrar_fecha_alta())
print(paciente1.mostrar_historial_enfermedades())
print(paciente1.mostrar_medicamentos_administrados())
print(paciente1.mostrar_alergias())

paciente1.actualizar_nombres('marina ines')
paciente1.actualizar_apellidos('carretero lorenzo')
paciente1.actualizar_edad(31)
paciente1.actualizar_dni(38923741)
paciente1.actualizar_telefono(1148237381)
paciente1.actualizar_domicilio('santa maria de oro 211')
paciente1.actualizar_localidad('temperley')
paciente1.actualizar_prepaga('swiss medical')
paciente1.agregar_enfermedad('diarrea')
paciente1.agregar_enfermedad('gripe')
paciente1.eliminar_enfermedad('diarrea')
paciente1.agregar_medicamento_administrado('ibuprofeno')
paciente1.agregar_medicamento_administrado('tafirol')
paciente1.eliminar_medicamento_administrado('ibuprofeno')

print(paciente1.mostrar_nombres())
print(paciente1.mostrar_apellidos())
print(paciente1.mostrar_edad())
print(paciente1.mostrar_dni())
print(paciente1.mostrar_telefono())
print(paciente1.mostrar_domicilio())
print(paciente1.mostrar_localidad())
print(paciente1.mostrar_fecha_alta())
print(paciente1.mostrar_historial_enfermedades())
print(paciente1.mostrar_medicamentos_administrados())
print(paciente1.mostrar_alergias()) 
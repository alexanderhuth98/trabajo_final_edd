from models.paciente import Paciente

class PacienteMetodos(Paciente):
    """
    Clase que contiene métodos adicionales para manejar la información del paciente.
    """

def __str__(self):
        """
        Devuelve una representación legible del objeto Paciente.

        Returns:
            str: Representación en forma de texto del paciente.
        """
        return (
            f"Nombre/s: {self.nombres_paciente}\n"
            f"Apellido/s: {self.apellidos_paciente}\n"
            f"Edad: {self.edad}\n"
            f"DNI: {self.dni}\n"
            f"Teléfono: {self.telefono_paciente}\n"
            f"Domicilio: {self.domicilio_paciente}\n"
            f"Localidad: {self.localidad_paciente}\n"
            f"Prepaga: {self.prepaga.title()}\n"
            f"Fecha de alta: {self.fecha_alta}\n"
            f"Historial: {self.historial_paciente}\n"
            f"Alergias: {self.alergias}\n"
        )

    # Métodos para mostrar información del paciente.
def mostrar_nombres(self):
        """
        Devuelve el nombre del paciente.

        Returns:
            str: Nombre del paciente en formato de título.
        """
        return f"Nombre/s paciente: {self.nombres_paciente.title()}."

def mostrar_apellidos(self):
        """
        Devuelve el apellido del paciente.

        Returns:
            str: Apellido del paciente en mayúsculas.
        """
        return f"Apellido/s paciente: {self.apellidos_paciente.upper()}."

    # Métodos adicionales (getters y setters) para actualizar información.
def actualizar_nombres(self, nuevos_nombres):
        """
        Actualiza el nombre del paciente.

        Args:
            nuevos_nombres (str): Nuevo nombre del paciente.

        Returns:
            str: Mensaje indicando el resultado de la operación.
        """
        if not nuevos_nombres:
            return "Error: el nombre no puede estar vacío."
        elif nuevos_nombres == self.nombres_paciente:
            return "Error: el nombre ingresado es idéntico al actual."
        self.nombres_paciente = nuevos_nombres
        return f"Nombre actualizado a: {self.nombres_paciente.title()}"

def actualizar_apellidos(self, nuevos_apellidos):
        """
        Actualiza el apellido del paciente.

        Args:
            nuevos_apellidos (str): Nuevo apellido del paciente.

        Returns:
            str: Mensaje indicando el resultado de la operación.
        """
        if not nuevos_apellidos:
            return "Error: el apellido no puede estar vacío."
        elif nuevos_apellidos == self.apellidos_paciente:
            return "Error: el apellido ingresado es idéntico al actual."
        self.apellidos_paciente = nuevos_apellidos
        return f"Apellido actualizado a: {self.apellidos_paciente.upper()}"

def mostrar_edad(self):
        """
        Devuelve una representación en forma de cadena de la edad del/la paciente.

        Returns:
            str: Una cadena con la edad del/la paciente.
        """
        return f'Edad: {self.edad} años.'

def actualizar_edad(self, nueva_edad):
        """
        Actualiza la edad del/la paciente.

        Args:
            nueva_edad (int): La nueva edad del/la paciente.

        Returns:
            str: Mensaje indicando el resultado de la actualización.
        """
        if nueva_edad <= 0:
            return "Error: La edad debe ser un número positivo."
        elif nueva_edad == self.edad:
            return "Error: La nueva edad ingresada es idéntica a la actual."
        else:
            self.edad = nueva_edad
            return f'Edad actualizada: {self.edad} años.'

def mostrar_dni(self):
        """
        Devuelve una representación en forma de cadena del DNI del/la paciente.

        Returns:
            str: Una cadena con el DNI del/la paciente.
        """
        return f'DNI: {self.dni}.'

def actualizar_dni(self, nuevo_dni):
        """
        Actualiza el DNI del/la paciente.

        Args:
            nuevo_dni (str): El nuevo DNI del/la paciente.

        Returns:
            str: Mensaje indicando el resultado de la actualización.
        """
        if nuevo_dni == "":
            return "Error: El DNI no puede estar vacío."
        elif nuevo_dni == self.dni:
            return "Error: El DNI ingresado es idéntico al actual."
        else:
            self.dni = nuevo_dni
            return f'DNI actualizado: {self.dni}.'

def mostrar_telefono(self):
        """
        Devuelve una representación en forma de cadena del teléfono del/la paciente.

        Returns:
            str: Una cadena con el teléfono del/la paciente.
        """
        return f'Teléfono: {self.telefono_paciente}.'

def actualizar_telefono(self, nuevo_telefono):
        """
        Actualiza el teléfono del/la paciente.

        Args:
            nuevo_telefono (str): El nuevo teléfono del/la paciente.

        Returns:
            str: Mensaje indicando el resultado de la actualización.
        """
        if nuevo_telefono == "":
            return "Error: El teléfono no puede estar vacío."
        elif nuevo_telefono == self.telefono_paciente:
            return "Error: El teléfono ingresado es idéntico al actual."
        else:
            self.telefono_paciente = nuevo_telefono
            return f'Teléfono actualizado: {self.telefono_paciente}.'

def mostrar_domicilio(self):
        """
        Devuelve una representación en forma de cadena del domicilio del/la paciente.

        Returns:
            str: Una cadena con el domicilio del/la paciente.
        """
        return f'Domicilio: {self.domicilio_paciente}.'

def actualizar_domicilio(self, nuevo_domicilio):
        """
        Actualiza el domicilio del/la paciente.

        Args:
            nuevo_domicilio (str): El nuevo domicilio del/la paciente.

        Returns:
            str: Mensaje indicando el resultado de la actualización.
        """
        if nuevo_domicilio == "":
            return "Error: El domicilio no puede estar vacío."
        elif nuevo_domicilio == self.domicilio_paciente:
            return "Error: El domicilio ingresado es idéntico al actual."
        else:
            self.domicilio_paciente = nuevo_domicilio
            return f'Domicilio actualizado: {self.domicilio_paciente}.'

def mostrar_localidad(self):
        """
        Devuelve una representación en forma de cadena de la localidad del/la paciente.

        Returns:
            str: Una cadena con la localidad del/la paciente.
        """
        return f'Localidad: {self.localidad_paciente}.'

def actualizar_localidad(self, nueva_localidad):
        """
        Actualiza la localidad del/la paciente.

        Args:
            nueva_localidad (str): La nueva localidad del/la paciente.

        Returns:
            str: Mensaje indicando el resultado de la actualización.
        """
        if nueva_localidad == "":
            return "Error: La localidad no puede estar vacía."
        elif nueva_localidad == self.localidad_paciente:
            return "Error: La localidad ingresada es idéntica a la actual."
        else:
            self.localidad_paciente = nueva_localidad
            return f'Localidad actualizada: {self.localidad_paciente}.'

def mostrar_prepaga(self):
        """
        Devuelve una representación en forma de cadena de la prepaga del/la paciente.

        Returns:
            str: Una cadena con la prepaga del/la paciente.
        """
        return f'Prepaga: {self.prepaga}.'

def actualizar_prepaga(self, nueva_prepaga):
        """
        Actualiza la prepaga del/la paciente.

        Args:
            nueva_prepaga (str): La nueva prepaga del/la paciente.

        Returns:
            str: Mensaje indicando el resultado de la actualización.
        """
        if nueva_prepaga == "":
            return "Error: La prepaga no puede estar vacía."
        elif nueva_prepaga == self.prepaga:
            return "Error: La prepaga ingresada es idéntica a la actual."
        else:
            self.prepaga = nueva_prepaga
            return f'Prepaga actualizada: {self.prepaga}.'

def mostrar_prioridad(self):
        """
        Devuelve una representación en forma de cadena de la prioridad del/la paciente.

        Returns:
            str: Una cadena con la prioridad del/la paciente.
        """
        return f'Prioridad: {self.prioridad}.'

def actualizar_prioridad(self, nueva_prioridad):
        """
        Actualiza la prioridad del/la paciente.

        Args:
            nueva_prioridad (int): El nuevo nivel de prioridad del/la paciente.

        Returns:
            str: Mensaje indicando el resultado de la actualización.
        """
        if nueva_prioridad < 0:
            return "Error: La prioridad debe ser un número positivo."
        elif nueva_prioridad == self.prioridad:
            return "Error: La prioridad ingresada es idéntica a la actual."
        else:
            self.prioridad = nueva_prioridad
            return f'Prioridad actualizada: {self.prioridad}.'

    # Función recursiva para buscar enfermedades.
def busqueda_enfermedad_recurrente(self, historial, clave, resultado=None):
        """
        Función recursiva para buscar enfermedades o medicamentos en el historial del paciente.

        Args:
            historial (dict): Diccionario con enfermedades como claves y medicamentos como valores.
            clave (str): Enfermedad o medicamento a buscar.
            resultado (list): Lista acumulativa con las coincidencias encontradas.

        Returns:
            dict: Resultados con el total de apariciones y detalles encontrados.
        """
        if resultado is None:
            resultado = []

        if not historial:  # Caso base: si el historial está vacío
            return {
                "total_apariciones": len(resultado),
                "detalles": resultado
            }

        # Extraer un elemento del historial
        enfermedad, medicamento = next(iter(historial.items()))

        # Verificar si la clave coincide con la enfermedad o el medicamento
        if clave.lower() in enfermedad.lower() or clave.lower() in medicamento.lower():
            resultado.append({"enfermedad": enfermedad, "medicamento": medicamento})

        # Preparar el resto del historial excluyendo la clave actual
        resto_historial = dict(list(historial.items())[1:])

        # Llamada recursiva con el resto del historial
        return self.busqueda_enfermedad_recurrente(resto_historial, clave, resultado)

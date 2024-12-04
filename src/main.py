from paciente import Paciente
from paciente_metodos import PacienteMetodos
from arbol_binario import ArbolBinarioBusqueda

def menu_principal():
    menu = """
Menú Principal:
Pacientes:
(1) Agregar paciente
(2) Mostrar información de un paciente
(3) Modificar atributos de un paciente
(4) Eliminar paciente

Árbol Binario:
(5) Mostrar árbol binario (in-order)
(6) Agregar paciente al árbol binario
(7) Eliminar paciente del árbol binario

Árbol General:
(8) Mostrar información del árbol general

Cola de Prioridad:
(9) Mostrar cola de prioridad
(10) Agregar paciente a la cola de prioridad
(11) Eliminar paciente de la cola de prioridad

Historial:
(12) Agregar enfermedad al historial de un paciente

(13) Salir
"""
    print(menu)
    opcion = input("Seleccione una opción del menú: ")

    while opcion != "13":
        if opcion == "1":
            print("Agregar paciente")
            nuevo_paciente = Paciente()
            print(nuevo_paciente)
        elif opcion == "2":
            print("Mostrar información de un paciente")
            PacienteMetodos.mostrar_nombres()
            PacienteMetodos.mostrar_apellidos()
            PacienteMetodos.mostrar_edad()
            PacienteMetodos.mostrar_dni()
            PacienteMetodos.mostrar_telefono()
            PacienteMetodos.mostrar_domicilio()
            PacienteMetodos.mostrar_localidad()
            PacienteMetodos.mostrar_prepaga()
            PacienteMetodos.mostrar_prioridad()
        elif opcion == "3":
            print("Modificar atributos de un paciente")

            submenu = """
            (1) Actualizar nombre
            (2) Actualizar apellido
            (3) Actualizar edad
            (4) Actualizar dni
            (5) Actualizar telefono
            (6) Actualizar domicilio
            (7) Actualizar localidad
            (8) Actualizar prepaga
            (9) Actualizar prioridad
            """
            print(submenu)
            PacienteMetodos.actualizar_nombres()
            PacienteMetodos.actualizar_apellidos()
            PacienteMetodos.actualizar_edad()
            PacienteMetodos.actualizar_dni()
            PacienteMetodos.actualizar_telefono()
            PacienteMetodos.actualizar_domicilio()
            PacienteMetodos.actualizar_localidad()
            PacienteMetodos.actualizar_prepaga()
            PacienteMetodos.actualizar_prioridad()
        elif opcion == "4":
            print("Eliminar paciente")
            nuevo_paciente = ""
        elif opcion == "5":
            print("Mostrar árbol binario (in-order)")
            ArbolBinarioBusqueda.imprimir_inorder()
        elif opcion == "6":
            print("Agregar paciente al árbol binario")
            ArbolBinarioBusqueda.insertar()
        elif opcion == "7":
            print("Eliminar paciente del árbol binario")
            ArbolBinarioBusqueda.eliminar()
        elif opcion == "8":
            print("Mostrar información del árbol general")
            ArbolBinarioBusqueda.mostrar_arb()
        elif opcion == "9":
            print("Mostrar cola de prioridad")
            ArbolBinarioBusqueda.cola.mostrar()
        elif opcion == "10":
            print("Agregar paciente a la cola de prioridad")
            ArbolBinarioBusqueda.cola.mostrar()
        elif opcion == "11":
            print("Eliminar paciente de la cola de prioridad")
            ArbolBinarioBusqueda.cola.extraer()
        elif opcion == "12":
            print("Agregar enfermedad al historial de un paciente")
            ArbolBinarioBusqueda.agregar_enfermedad()
        else:
            print("Opción inválida, por favor intente de nuevo.")
        
        print(menu)
        opcion = input("Seleccione una opción del menú: ")

    print("Gracias por usar el sistema.")

# Llamada al menú principal
menu_principal()

from models.paciente_metodos import cargar_paciente , modificar_un_paciente , eliminar_un_paciente , agregar_al_historial
from trees.arbol_binario import ArbolBinarioBusqueda
from graphs.grafo import Grafo
from graphs.grafo_metodos import agregar_vertice_grafo , agregar_arista_grafo , ver_todo_grafo 


menu="""
(1) Cargar pacientes
(2) Mostrar pacientes 
(3) Modificar paciente
(4) Eliminar paciente
(5) Agregar al historial
(6) Cargar hospital
(7) Cargar distancia entre hospitales
(8) Mostrar red hospitales para translado de urgencia
(9) Salir
"""

print (menu)
opcion= int(input("ingrese una opcion del menu:"))
while opcion != 9:
    
    if(opcion==1):
        print('Elegiste la opcion 1')
        cargar_paciente()
        
    elif(opcion==2):
        print('Elegiste la opcion 2')
        ArbolBinarioBusqueda().imprimir_inorder()
    
    elif(opcion==3):
        print('Elegiste la opcion 3')
        modificar_un_paciente()
        
    elif(opcion==4):
        print('Elegiste la opcion 4')
        eliminar_un_paciente()
    
    elif(opcion==5):
        print('Elegiste la opcion 5')
        agregar_al_historial()
        
    
    elif(opcion==6):
        print('Elegiste la opcion 6')
        agregar_vertice_grafo()
        f'Hospitales cargados: {Grafo.mostrar_grafo()}'
        
    elif(opcion==7):
        print('Elegiste la opcion 7')
        agregar_arista_grafo()
        
    elif(opcion==8):
        print('Elegiste la opcion 8')
        ver_todo_grafo()
        
    
    else:
        print('No elegiste una opcion valida')
    
    print(menu)
    opcion = int(input('ingrese una opcion del menu:'))
        
	

	
print ("Gracias por usar el Sistema")
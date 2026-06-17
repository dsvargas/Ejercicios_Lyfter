# Importamos los módulos que te solicita el ejercicio
from Menu import menu
from Actions import actions
from Data import data

def main():
    
    
    # Esta lista global en memoria guardará los diccionarios de cada estudiante.
    # Al pasarla como argumento a las funciones, todos los módulos compartirán la misma info.
    students_list = []
    
    print("=========================================")
    print(" Sistema de Control Académico Iniciado ")
    print("=========================================")
    
    while True:
        # 1. Mostramos el menú y capturamos la opción ya validada (gracias al módulo menu)
        opcion = menu.mostrar_y_validar_menu()
        
        # 2. Evaluamos la opción seleccionada y delegamos la tarea al módulo correspondiente
        if opcion == '1':
            # Ingresar n cantidad de estudiantes
            actions.ingresar_estudiantes(students_list)
            
        elif opcion == '2':
            # Ver la información de todos los estudiantes
            actions.ver_todos_estudiantes(students_list)
            
        elif opcion == '3':
            # Ver el top 3 de estudiantes con mejor promedio
            actions.ver_top_tres_estudiantes(students_list)
            
        elif opcion == '4':
            # Ver el promedio general de la institución
            actions.ver_promedio_general(students_list)
            
        elif opcion == '5':
            # Exportar datos actuales a un archivo CSV
            data.exportar_a_csv(students_list)
            
        elif opcion == '6':
            # Importar datos desde un archivo CSV previo
            # Asignamos el retorno a la lista para actualizar los datos en memoria
            students_list = data.importar_desde_csv()
            
        elif opcion == '7':
            # Salida segura del sistema
            print("\nGracias por utilizar el sistema académico. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
from os import name
import os
from Actions.Actions import insert_students, show_top_students, show_average_grade, show_students, delete_students, show_failed_students
from Data.Student import  insert_students_to_csv, get_students_from_csv

import csv

def show_menu():
    while True:
        print("\nBienvenido al sistema de control de estudiantes")
        print("1. Registrar estudiantes")
        print("2. Ver el top 3 de los estudiantes con la mejor nota promedio")
        print("3. Ver la nota promedio entre las notas de todos los estudiantes registrados en el sistema")
        print("4. Ver la lista de estudiantes registrados en el sistema")
        print("5. Modificar un estudiante registrado en el sistema")
        print("6. Eliminar un estudiante registrado en el sistema")
        print("7. Exportar la lista de estudiantes a un archivo CSV")
        print("8. Importar la lista de estudiantes desde un archivo CSV")
        print("9. Ver estudiantes reprobados")
        print("10. Salir")

        choice = input("Seleccione una opción: ")

        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            return choice
        else:
            print("Opción no válida. Por favor, seleccion11e una opción del 1 al 10.")

def main_menu():
    students_list = []

    while True:
        choice = show_menu()

        if choice == '1':
            insert_students(students_list)
        elif choice == '2':
            show_top_students(students_list)
        elif choice == '3':
            
            show_average_grade(students_list)
        elif choice == '4':
            
            show_students(students_list)
        elif choice == '5':  
            #modify_student(students_list)
            print("En proceso.")
        elif choice == '6':
            delete_students(students_list)
        elif choice == '7':
            export_choice = input("¿Desea exportar la lista de estudiantes a un archivo CSV antes de salir? (s/n): ").strip().lower()
            if export_choice == 's':
                file_path = input("Ingrese la ruta del archivo CSV donde desea exportar la lista de estudiantes: ")
                file_path = file_path.strip() + ".csv" if not file_path.endswith(".csv") else file_path

                insert_students_to_csv(file_path,students_list)
                print("Lista de estudiantes exportada a CSV. Saliendo del programa.")
            else:
                print("Saliendo del programa sin exportar.")
            break
        elif choice == '8':
            import_choice = input("¿Desea importar la lista de estudiantes desde un archivo CSV? (s/n): ").strip().lower()
            
            if import_choice == 's':
                # Iniciamos el bucle de validación persistente
                while True:
                    file_path = input("Ingrese la ruta o nombre del archivo CSV: ").strip()
                    
                    # Si el usuario no escribió la extensión, se la agregamos de forma limpia
                    if not file_path.lower().endswith(".csv"):
                        file_path = file_path + ".csv"
                    
                    # Verificamos si el archivo físico realmente existe en el disco duro
                    if os.path.exists(file_path):
                        students_list = get_students_from_csv(file_path)
                        print("✅ Lista de estudiantes importada exitosamente desde CSV.")
                        break  # Rompe el while únicamente si el archivo existe y fue leído
                    else:
                        
                        print("❌ El archivo '{}' no existe. Por favor, intente de nuevo.".format(file_path))
                        # Al no haber un break aquí, el while vuelve a pedir el input()
            else:
                print("No se importó ningún archivo CSV.")

        elif choice == '9':
            show_failed_students(students_list)
        elif choice == '10':
            print("Gracias por usar el sistema de control de estudiantes")
            break
        else:
            print("Existe un error en la selección de la opción. Por favor, intente nuevamente.")

# Importamos los módulos que te solicita el ejercicio
from Actions.Actions import insert_students, show_top_students, show_average_grade, show_students
from Data.Students import insert_students_to_csv, get_students_from_csv, modify_students_to_csv, delete_students_to_csv 

def show_menu():
    print("\nBienvenido al sistema de control de estudiantes")
    print("1. Registrar estudiantes")
    print("2. Ver el top 3 de los estudiantes con la mejor nota promedio")
    print("3. Ver la nota promedio entre las notas de todos los estudiantes registrados en el sistema")
    print("4. Ver la lista de estudiantes registrados en el sistema")
    print("5. Modificar un estudiante registrado en el sistema")
    print("6. Eliminar un estudiante registrado en el sistema (aun en proceso)")
    print("7. Salir")
    while True:
        choice = input("Seleccione una opción: ")
        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")
            return None
        return choice

def main_menu():
    students_file = "students.csv"
    students_list = get_students_from_csv(students_file)

    while True:
        choice = show_menu()

        if choice == '1':
            insert_students(students_list)
            insert_students_to_csv(students_file, students_list)
        elif choice == '2':
            student_list = get_students_from_csv("students.csv")  # Aseguramos que tenemos los datos más recientes antes de mostrar el top
            show_top_students(student_list)
        elif choice == '3':
            student_list = get_students_from_csv("students.csv")  # Aseguramos que tenemos los datos más recientes antes de mostrar el promedio
            show_average_grade(student_list)
        elif choice == '4':
            student_list = get_students_from_csv("students.csv")  # Aseguramos que tenemos los datos más recientes antes de mostrar la lista
            show_students(students_list)
        elif choice == '5':  # Aseguramos que tenemos los datos más recientes antes de modificar
            modify_students_to_csv(students_file, student_list)
        elif choice == '6':
            delete_students_to_csv(students_file, students_list)
        elif choice == '7':
            print("Gracias por usar el sistema de control de estudiantes")
            break
        else:
            print("Existe un error en la selección de la opción. Por favor, intente nuevamente.")

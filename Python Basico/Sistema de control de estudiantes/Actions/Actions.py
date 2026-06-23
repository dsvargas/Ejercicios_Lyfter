import csv
from Data.Students import insert_students_to_csv, get_students_from_csv, modify_students_to_csv, delete_students_to_csv

def is_valid_name(prompt):
    while True:
        name = input(prompt).strip()
        if not all(char.isalpha() or char.isspace() for char in name):
            print("Error: El nombre solo puede contener letras y espacios.")
        else:
            return name
        
def is_valid_first_last_name(prompt):
    while True:
        first_last_name = input(prompt).strip()
        if not all(char.isalpha() or char.isspace() for char in first_last_name):
            print("Error: El primer apellido solo puede contener letras y espacios.")
        else:
            return first_last_name

def is_valid_second_last_name(prompt):
    while True:
        second_last_name = input(prompt).strip()
        if not all(char.isalpha() or char.isspace() for char in second_last_name):
            print("Error: El segundo apellido solo puede contener letras y espacios.")
        else:
            return second_last_name

def is_valid_section(prompt):
    """Valida que la sección tenga el formato correcto (ejemplo: 11B)."""
    while True:
        section = input(prompt).strip()
        if len(section) < 2 or not section[:-1].isdigit() or not section[-1].isalpha():
            print("Error: La sección debe tener el formato correcto (ejemplo: 11B).")
        else:
            return section

def read_positive_int(prompt):
    """Pide un número entero positivo y no para hasta que sea válido."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Error: El número debe ser mayor a cero.")
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

def read_valid_grade(prompt):
    """Pide una nota académica y valida que esté estrictamente entre 0 y 100."""
    while True:
        try:
            grade = int(input(prompt))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Error: La nota debe estar en el rango de 0 a 100.")
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido para la nota.")

def validate_student_existence(name, first_last_name, second_last_name,section):
    """Valida si un estudiante ya existe en la lista de estudiantes."""
    list_students = get_students_from_csv("students.csv")  # Aseguramos que tenemos los datos más recientes antes de validar
    for student in list_students:
        if (student["name"].lower() == name.lower() and
            student["first_last_name"].lower() == first_last_name.lower() and
            student["second_last_name"].lower() == second_last_name.lower() and
            student["section"].lower() == section.lower()):
            return True
    return False

def insert_students(list_students):
    """Maneja el flujo completo para registrar N cantidad de estudiantes."""
    # Usamos nuestra función de validación para obtener la cantidad de alumnos
    n = read_positive_int("Ingrese la cantidad de estudiantes a registrar: ")
    
    for i in range(n):
        print("\n--- Registrando estudiante {} de {} ---".format(i + 1, n))
        
        # Creamos un diccionario vacío exclusivo para este estudiante
        student = {}

        student["first_last_name"] = is_valid_first_last_name("Ingrese el primer apellido del estudiante: ")
        student["second_last_name"] = is_valid_second_last_name("Ingrese el segundo apellido del estudiante: ")
        student["name"] = is_valid_name("Ingrese el nombre del estudiante: ")

        student["section"] = is_valid_section("Ingrese la sección del estudiante (ejemplo: 11B): ").strip()
        
        # Captura de notas usando nuestra función validadora con try-except persistente
        student["spanish_grade"] = read_valid_grade("Ingrese la nota de español: ")
        student["english_grade"] = read_valid_grade("Ingrese la nota de inglés: ")
        student["social_grade"] = read_valid_grade("Ingrese la nota de sociales: ")
        student["science_grade"] = read_valid_grade("Ingrese la nota de ciencias: ")
        
        
        list_students.append(student)
        print("¡Estudiante registrado con éxito en el sistema!")

def show_students(students_list):
    for row in students_list:
        print(f"Nombre completo: {row['name']} {row['first_last_name']} {row['second_last_name']}")
        print(f"Sección: {row['section']}")
        print(f"Nota de español: {row['spanish_grade']}")
        print(f"Nota de inglés: {row['english_grade']}")
        print(f"Nota de sociales: {row['social_grade']}")
        print(f"Nota de ciencias: {row['science_grade']}")
        print("-" * 40)
    


def show_top_students(list_students):
    # Calcular el promedio para cada estudiante
    for student in list_students:
        # Convertimos cada nota a entero (int) para poder sumarlas matemáticamente
        nota_espanol = int(student["spanish_grade"])
        nota_ingles = int(student["english_grade"])
        nota_sociales = int(student["social_grade"])
        nota_ciencias = int(student["science_grade"])

        # Calculamos el total y el promedio de forma segura
        total = nota_espanol + nota_ingles + nota_sociales + nota_ciencias
        student["average"] = total / 4

    # Ordenar los estudiantes por promedio (de mayor a menor)
    sorted_students = sorted(list_students, key=lambda x: x["average"], reverse=True)

    # Mostrar el top 3
    print("\n--- Top 3 Estudiantes ---")
    for i, student in enumerate(sorted_students[:3], start=1):
        print(f"{i}. {student['name']} {student['first_last_name']} {student['second_last_name']} - Promedio: {student['average']:.2f}")

#Ver la nota promedio entre las notas de todos los estudiantes registrados en el sistema.
def show_average_grade(list_students):
    total_students = len(list_students)
    if total_students == 0:
        print("\nNo hay estudiantes registrados para calcular el promedio.")
        return

    total_spanish = sum(int(student["spanish_grade"]) for student in list_students)
    total_english = sum(int(student["english_grade"]) for student in list_students)
    total_social = sum(int(student["social_grade"]) for student in list_students)
    total_science = sum(int(student["science_grade"]) for student in list_students)

    average_spanish = total_spanish / total_students
    average_english = total_english / total_students
    average_social = total_social / total_students
    average_science = total_science / total_students

    print("\n--- Promedio de Notas ---")
    print(f"Promedio de español: {average_spanish:.2f}")
    print(f"Promedio de inglés: {average_english:.2f}")
    print(f"Promedio de sociales: {average_social:.2f}")
    print(f"Promedio de ciencias: {average_science:.2f}")

def modify_students(students_list):
    name = input("Ingrese el nombre del estudiante a modificar: ")
    first_last_name = input("Ingrese el primer apellido del estudiante a modificar: ")
    second_last_name = input("Ingrese el segundo apellido del estudiante a modificar: ")
    section = input("Ingrese la sección del estudiante a modificar: ")

    for student in students_list:
        if (student["name"].lower() == name.lower() and
            student["first_last_name"].lower() == first_last_name.lower() and
            student["second_last_name"].lower() == second_last_name.lower() and
            student["section"].lower() == section.lower()):
            
            print("Estudiante encontrado. Ingrese los nuevos datos:")
            student["name"] = is_valid_name("Ingrese el nuevo nombre del estudiante: ")
            student["first_last_name"] = is_valid_first_last_name("Ingrese el nuevo primer apellido del estudiante: ")
            student["second_last_name"] = is_valid_second_last_name("Ingrese el nuevo segundo apellido del estudiante: ")
            student["section"] = is_valid_section("Ingrese la nueva sección del estudiante (ejemplo: 11B): ").strip()
            student["spanish_grade"] = read_valid_grade("Ingrese la nueva nota de español: ")
            student["english_grade"] = read_valid_grade("Ingrese la nueva nota de inglés: ")
            student["social_grade"] = read_valid_grade("Ingrese la nueva nota de sociales: ")
            student["science_grade"] = read_valid_grade("Ingrese la nueva nota de ciencias: ")
            
            print("¡Estudiante modificado con éxito!")
            return

    print("No se encontró un estudiante con esos datos.")

def delete_students(students_list):
    name = input("Ingrese el nombre del estudiante a eliminar: ")
    first_last_name = input("Ingrese el primer apellido del estudiante a eliminar: ")
    second_last_name = input("Ingrese el segundo apellido del estudiante a eliminar: ")
    section = input("Ingrese la sección del estudiante a eliminar: ")
    if validate_student_existence(name, first_last_name, second_last_name, section):
        for i, student in enumerate(students_list):
            if (student["name"].lower() == name.lower() and
                student["first_last_name"].lower() == first_last_name.lower() and
                student["second_last_name"].lower() == second_last_name.lower() and
                student["section"].lower() == section.lower()):
                
                del students_list[i]
                print("¡Estudiante eliminado con éxito!")
                return

    print("No se encontró un estudiante con esos datos.")
import os
from Data.Student import Student

# --- (Tus funciones de validación de texto e inputs se quedan EXACTAMENTE igual) ---
def is_valid_name(prompt):
    while True:
        name = input(prompt).strip()
        if not all(char.isalpha() or char.isspace() for char in name):
            print("Error: El nombre solo puede contener letras.")
        else: return name
        
def is_valid_first_last_name(prompt):
    while True:
        first_last_name = input(prompt).strip()
        if not all(char.isalpha() or char.isspace() for char in first_last_name):
            print("Error: El primer apellido solo puede contener letras.")
        else: return first_last_name

def is_valid_second_last_name(prompt):
    while True:
        second_last_name = input(prompt).strip()
        if not all(char.isalpha() or char.isspace() for char in second_last_name):
            print("Error: El segundo apellido solo puede contener letras.")
        else: return second_last_name

def is_valid_section(prompt):
    while True:
        section = input(prompt).strip()
        if len(section) < 2 or not section[:-1].isdigit() or not section[-1].isalpha():
            print("Error: La sección debe tener el formato correcto (ejemplo: 11B).")
        else: return section

def read_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0: return value
            else: print("Error: El número debe ser mayor a cero.")
        except ValueError: print("Error: Por favor, ingrese un número entero válido.")

def read_valid_grade(prompt):
    while True:
        try:
            grade = int(input(prompt))
            if 0 <= grade <= 100: return grade
            else: print("Error: La nota debe estar en el rango de 0 a 100.")
        except ValueError: print("Error: Por favor, ingrese un número entero válido para la nota.")


# --- Funciones Adaptadas a POO ---

def validate_student_existence(list_of_students, name, first_last_name, second_last_name, section):
    """Valida la existencia usando atributos de objetos."""
    for student in list_of_students:
        if (student.name.lower() == name.lower() and
            student.first_last_name.lower() == first_last_name.lower() and
            student.second_last_name.lower() == second_last_name.lower() and
            student.section.lower() == section.lower()):
            return True
    return False


def insert_students(list_students):
    n = read_positive_int("Ingrese la cantidad de estudiantes a registrar: ")
    
    for i in range(n):
        print("\n--- Registrando estudiante {} de {} ---".format(i + 1, n))
        
        first_last_name = is_valid_first_last_name("Ingrese el primer apellido del estudiante: ")
        second_last_name = is_valid_second_last_name("Ingrese el segundo apellido del estudiante: ")
        name = is_valid_name("Ingrese el nombre del estudiante: ")
        section = is_valid_section("Ingrese la sección del estudiante (ejemplo: 11B): ").strip()

        if validate_student_existence(list_students, name, first_last_name, second_last_name, section):
            print("Error: Este estudiante ya está registrado en el sistema. No se puede duplicar.")
        else:
            spanish_grade = read_valid_grade("Ingrese la nota de español: ")
            english_grade = read_valid_grade("Ingrese la nota de inglés: ")
            social_grade = read_valid_grade("Ingrese la nota de sociales: ")
            science_grade = read_valid_grade("Ingrese la nota de ciencias: ")

            # Instanciamos el objeto con la clase Student
            new_student = Student(name, first_last_name, second_last_name, section, spanish_grade, english_grade, social_grade, science_grade)
            list_students.append(new_student)
            print("¡Estudiante registrado con éxito en el sistema!")


def show_students(students_list):
    if not students_list:
        print("\nNo hay estudiantes registrados.")
        return
    for student in students_list:
        print(f"Nombre completo: {student.name} {student.first_last_name} {student.second_last_name}")
        print(f"Sección: {student.section}")
        print(f"Nota de español: {student.spanish_grade}")
        print(f"Nota de inglés: {student.english_grade}")
        print(f"Nota de sociales: {student.social_grade}")
        print(f"Nota de ciencias: {student.science_grade}")
        print("-" * 40)


def show_top_students(list_students):
    if not list_students:
        print("\nNo hay estudiantes registrados para calcular el Top 3.")
        return
        
    # Ordenamos aprovechando el método interno get_average() del objeto
    sorted_students = sorted(list_students, key=lambda x: x.get_average(), reverse=True)

    print("\n--- Top 3 Estudiantes ---")
    for i, student in enumerate(sorted_students[:3], start=1):
        print(f"{i}. {student.name} {student.first_last_name} {student.second_last_name} - Promedio: {student.get_average():.2f}")


def show_average_grade(list_students):
    total_students = len(list_students)
    if total_students == 0:
        print("\nNo hay estudiantes registrados para calcular el promedio.")
        return

    total_spanish = sum(student.spanish_grade for student in list_students)
    total_english = sum(student.english_grade for student in list_students)
    total_social = sum(student.social_grade for student in list_students)
    total_science = sum(student.science_grade for student in list_students)

    print("\n--- Promedio de Notas ---")
    print(f"Promedio de español: {total_spanish / total_students:.2f}")
    print(f"Promedio de inglés: {total_english / total_students:.2f}")
    print(f"Promedio de sociales: {total_social / total_students:.2f}")
    print(f"Promedio de ciencias: {total_science / total_students:.2f}")


def show_failed_students(list_students):
    # Filtrado limpio usando el método interno is_failed()
    failed_students = [student for student in list_students if student.is_failed()]

    if not failed_students:
        print("\nNo hay estudiantes reprobados. 🎉")
        return

    print("\n--- Estudiantes Reprobados ---")
    for student in failed_students:
        print(f"Nombre completo: {student.name} {student.first_last_name} {student.second_last_name}")
        print(f"Sección: {student.section}")
        print(f"Nota de español: {student.spanish_grade}")
        print(f"Nota de inglés: {student.english_grade}")
        print(f"Nota de sociales: {student.social_grade}")
        print(f"Nota de ciencias: {student.science_grade}")
        print("-" * 40)


def modify_students(students_list):
    name = input("Ingrese el nombre del estudiante a modificar: ")
    first_last_name = input("Ingrese el primer apellido del estudiante a modificar: ")
    second_last_name = input("Ingrese el segundo apellido del estudiante a modificar: ")
    section = input("Ingrese la sección del estudiante a modificar: ")

    for student in students_list:
        if (student.name.lower() == name.lower() and
            student.first_last_name.lower() == first_last_name.lower() and
            student.second_last_name.lower() == second_last_name.lower() and
            student.section.lower() == section.lower()):
            
            print("Estudiante encontrado. Ingrese los nuevos datos:")
            student.name = is_valid_name("Ingrese el nuevo nombre del estudiante: ")
            student.first_last_name = is_valid_first_last_name("Ingrese el nuevo primer apellido del estudiante: ")
            student.second_last_name = is_valid_second_last_name("Ingrese el nuevo segundo apellido del estudiante: ")
            student.section = is_valid_section("Ingrese la nueva sección del estudiante (ejemplo: 11B): ").strip()
            student.spanish_grade = read_valid_grade("Ingrese la nueva nota de español: ")
            student.english_grade = read_valid_grade("Ingrese la nueva nota de inglés: ")
            student.social_grade = read_valid_grade("Ingrese la nueva nota de sociales: ")
            student.science_grade = read_valid_grade("Ingrese la nueva nota de ciencias: ")
            
            print("¡Estudiante modificado con éxito!")
            return

    print("No se encontró un estudiante con esos datos.")


def delete_students(students_list):
    name = input("Ingrese el nombre del estudiante a eliminar: ")
    first_last_name = input("Ingrese el primer apellido del estudiante a eliminar: ")
    second_last_name = input("Ingrese el segundo apellido del estudiante a eliminar: ")
    section = input("Ingrese la sección del estudiante a eliminar: ")
    
    if validate_student_existence(students_list, name, first_last_name, second_last_name, section):
        for student in students_list:
            if (student.name.lower() == name.lower() and
                student.first_last_name.lower() == first_last_name.lower() and
                student.second_last_name.lower() == second_last_name.lower() and
                student.section.lower() == section.lower()):
                
                students_list.remove(student) # remove() es más seguro que del con índices
                print("¡Estudiante eliminado con éxito!")
                return

    print("No se encontró un estudiante con esos datos.")
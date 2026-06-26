import csv

class Student:
    def __init__(self, name, first_last_name, second_last_name, section, spanish_grade, english_grade, social_grade, science_grade):
        self.name = name
        self.first_last_name = first_last_name
        self.second_last_name = second_last_name
        self.section = section
        
        self.spanish_grade = int(spanish_grade)
        self.english_grade = int(english_grade)
        self.social_grade = int(social_grade)
        self.science_grade = int(science_grade)

    def get_average(self):
        """Calcula el promedio del estudiante."""
        total = self.spanish_grade + self.english_grade + self.social_grade + self.science_grade
        return total / 4

    def is_failed(self):
        """Retorna True si tiene al menos una nota menor a 60."""
        return (self.spanish_grade < 60 or 
                self.english_grade < 60 or 
                self.social_grade < 60 or 
                self.science_grade < 60)

    def to_dict(self):
        """Convierte los atributos del objeto a un diccionario para escribir en el CSV."""
        return {
            "name": self.name,
            "first_last_name": self.first_last_name,
            "second_last_name": self.second_last_name,
            "section": self.section,
            "spanish_grade": self.spanish_grade,
            "english_grade": self.english_grade,
            "social_grade": self.social_grade,
            "science_grade": self.science_grade
        }


def insert_students_to_csv(file_path, students_list):
    headers = ["name", "first_last_name", "second_last_name", "section", "spanish_grade", "english_grade", "social_grade", "science_grade"]
    try:
        with open(file_path, mode='w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            
            # Convertimos la lista de objetos Student a diccionarios usando .to_dict() antes de guardar
            dict_list = [student.to_dict() for student in students_list]
            writer.writerows(dict_list)
        
        print("\nSuccess: Data successfully saved to '{}'!".format(file_path))
        return True
    except IOError:
        print("\nError: Could not write to the file '{}'.".format(file_path))
        return False


def get_students_from_csv(file_path):
    students = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                
                new_student = Student(
                    name=row['name'],
                    first_last_name=row['first_last_name'],
                    second_last_name=row['second_last_name'],
                    section=row['section'],
                    spanish_grade=row['spanish_grade'],
                    english_grade=row['english_grade'],
                    social_grade=row['social_grade'],
                    science_grade=row['science_grade']
                )
                students.append(new_student)
        return students
    except IOError:
        print("\nError: Could not read the file '{}'.".format(file_path))
    return students
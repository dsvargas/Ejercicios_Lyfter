import csv

def insert_students_to_csv(file_path, students_list):
    headers = ["name", "first_last_name", "second_last_name", "section", "spanish_grade", "english_grade", "social_grade", "science_grade"]
    
    try:
        with open(file_path, mode='w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(students_list)
        
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
                students.append(row)
        return students
    except IOError:
        print("\nError: Could not read the file '{}'.".format(file_path))
    return students

def modify_students_to_csv(file_path, students_list):
    headers = ["name", "first_last_name", "second_last_name", "section", "spanish_grade", "english_grade", "social_grade", "science_grade"]
    
    try:
        with open(file_path, mode='w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(students_list)
        
        print("\nSuccess: Data successfully modified in '{}'!".format(file_path))
        return True
    except IOError:
        print("\nError: Could not write to the file '{}'.".format(file_path))
        return False
    
def delete_students_to_csv(file_path, students_list):
    headers = ["name", "first_last_name", "second_last_name", "section", "spanish_grade", "english_grade", "social_grade", "science_grade"]
    try:
        with open(file_path, mode='w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(students_list)
        
        print("\nSuccess: Data successfully deleted in '{}'!".format(file_path))
        return True
    except IOError:
        print("\nError: Could not write to the file '{}'.".format(file_path))
        return False
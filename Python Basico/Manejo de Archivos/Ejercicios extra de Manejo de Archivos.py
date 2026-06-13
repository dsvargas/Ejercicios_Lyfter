# Cree un programa que lea un archivo con texto línea por línea, quite los saltos de línea (\n) y escriba todo el contenido en un solo renglón en un nuevo archivo

def read_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        return lines
    
    except:
        print("Error: Could not read the input file.")
        return ""
    
def cut_lines(lines_to_read):
    try:
        single_line_content = ""
        for line in lines_to_read:
            # .strip() remueve el '\n' al final de la línea actual
            clean_line = line.strip()
            #Acumulamos
            single_line_content = single_line_content + clean_line + " "

        return single_line_content

    except:
        print("Error: Could not join the file.")
        return ""
    


def save_result(content_to_save, output_file_name):
    try:
        with open(output_file_name, "w", encoding="utf-8") as output_file:
            output_file.write(content_to_save)
            print("Success: Content successfully saved")
    except:
        print("Error: Could not write to the output file")

content = read_lines('pruebas.txt')
lines_to_read = cut_lines(content)
save_result(lines_to_read, "output.txt")
 
# Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.
def count_words_in_file(content_list):
    try:
        total_words = 0
        for line in content_list:
        # .split() divide la línea actual en palabras
            words_in_line = line.split()
        
        # len() cuenta cuántas palabras hay en esta línea específica
        # y las sumamos a nuestro acumulador total
            total_words += len(words_in_line)
        
        print("Total words found: {}".format(total_words))
        return total_words
    except:
       print("Error could not count the words")
    
content = read_lines('pruebas.txt')
count_words_in_file(content)

# Cree un programa que:
# Lea un archivo línea por línea
# Convierta cada línea a mayúsculas
#Escriba el contenido en un nuevo archivo
# #
def convert_to_uppercase(content):
    try:
        uppercase_lines = []
        for line in content:
            # .upper() convierte todo el texto del renglón a mayúsculas
            line_in_uppercase = line.upper()
            # Guardamos la línea modificada en nuestra nueva lista
            uppercase_lines.append(line_in_uppercase)
        
        return uppercase_lines
    except:
        print("Error could not convert the words to uppercase")

content = read_lines('pruebas.txt')     
converted_content = convert_to_uppercase(content)
save_result("".join(converted_content), "output_uppercase.txt")

# Cree un programa que:
# Pida al usuario una línea de texto
# Agregue esa línea al final de un archivo existente
# Si el archivo no existe, lo crea automáticamente
def add_line_to_file(file_name):
    try:
        user_input = input("Please enter a line of text to add to the file: ")
        with open(file_name, 'a', encoding="utf-8") as file:
            file.write(user_input + "\n")
            print("Success: Line added to the file.")
    except:
        print("Error: Could not write to the file.")

add_line_to_file("pruebas.txt")

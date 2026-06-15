import csv

# 1 Cree un programa que abra un archivo .csv con la información de videojuegos (el que fue generado en el ejercicio 1)

def read(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            lines = list(reader)  # Convertimos el reader a una lista para poder iterar varias veces
            return lines
    except FileNotFoundError:
        print("Error: El archivo '{}' no existe. Ejecute el registro primero.".format(file_path))
        return []
def display_games(game_lines):
    """Prints each game from the loaded CSV list in a human-readable format."""
    # Si la lista está vacía (hubo error o archivo vacío), detenemos la función
    if not game_lines:
        return

    try:
        # El primer elemento (índice 0) son siempre los encabezados.
        headers = game_lines[0]
        
        print("\n=== Lista de Videojuegos Registrados ===")
        
        # 2. Recorremos la lista desde el índice 1 en adelante [1:] para saltarnos las cabeceras
        for row in game_lines[1:]:
            if row:
                print("Nombre: {}".format(row[0]))
                print("Género: {}".format(row[1]))
                print("Desarrollador: {}".format(row[2]))
                print("Clasificación: {}".format(row[3]))
                print("-" * 30)

    except IndexError:
        print("Error: El formato del archivo no es el esperado.")

#2 Cree un programa que abra un archivo .csv con la información de videojuego
# Lea el archivo CSV de videojuegos
# Pida al usuario una clasificación ESRB (por ejemplo: "T")
#Muestre todos los videojuegos que tengan esa clasificación #
def filter_games_by_rating(game_lines, rating):
    try:
        # Saltamos la primera línea, encabezados
        headers = game_lines[0]
        
        print("\n=== Videojuegos con clasificación '{}' ===".format(rating))
        for row in game_lines[1:]:
            if row and row[3].strip().upper() == rating.upper():
                print("Nombre: {}".format(row[0]))
                print("Género: {}".format(row[1]))
                print("Desarrollador: {}".format(row[2]))
                print("Clasificación: {}".format(row[3]))
                print("-" * 30) # Línea divisoria entre juegos

    except FileNotFoundError:
        print("Error: El archivo '{}' no existe. Ejecute el registro primero.".format(file_path))

# 3 Cree un programa que abra un archivo .csv con la información de videojuego
# Lea el archivo CSV de videojuegos
# Cuente cuántos videojuegos hay de cada género
# Muestre el resultado de forma ordenada #

def count_games_by_genre(game_lines):
    genre_count = {}
    
    try:
        # Saltamos la primera línea, encabezados
        headers = game_lines[0]

        for row in game_lines[1:]:
            if row:
                genre = row[1].strip()
                if genre in genre_count:
                    genre_count[genre] += 1
                else:
                    genre_count[genre] = 1
        
        print("\n=== Conteo de Videojuegos por Género ===")
        for genre, count in sorted(genre_count.items()):
            print("{}: {}".format(genre, count))

    except FileNotFoundError:
        print("Error: El archivo '{}' no existe. Ejecute el registro primero.".format(file_path))

#4 Cree un programa que abra un archivo .csv con la información de videojuego
# Lea el archivo CSV de videojuegos 
# Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
#uestre todos los videojuegos desarrollados por esa empresa en formato legible: #
def filter_games_by_developer(game_lines, developer):
    try:
        # Saltamos la primera línea, encabezados
        headers = game_lines[0]
        
        print("\n=== Videojuegos desarrollados por '{}' ===".format(developer))
        for row in game_lines[1:]:
            if row and row[2].strip().upper() == developer.upper():
                print("Nombre: {}".format(row[0]))
                print("Género: {}".format(row[1]))
                print("Desarrollador: {}".format(row[2]))
                print("Clasificación: {}".format(row[3]))
                print("-" * 30) # Línea divisoria entre juegos

    except FileNotFoundError:
        print("Error: El archivo '{}' no existe. Ejecute el registro primero.".format(file_path))




if __name__ == "__main__":
    game_lines = read("videogames.csv")
    if game_lines:
        display_games(game_lines)
        filter_games_by_rating(game_lines, input("\nIngrese una clasificación ESRB para filtrar (por ejemplo: 'T'): "))
        count_games_by_genre(game_lines)
        filter_games_by_developer(game_lines, input("\nIngrese el nombre de un desarrollador para filtrar (por ejemplo: 'Ubisoft'): "))
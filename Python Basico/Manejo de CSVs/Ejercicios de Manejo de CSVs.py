#Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
# Debe incluir:  Nombre,  Género, Desarrollador, Clasificación ESRB
# 
# 
# 
# 
# #
import csv

def get_video_game_data():
    """Asks the user for data and returns a dictionary with the videogame info."""
    print("\n--- Enter Video Game Details ---")
    name = input("Name: ")
    genre = input("Genre: ")
    developer = input("Developer: ")
    esrb = input("ESRB Rating: ")
    
    # Guardamos los datos en un diccionario usando los mismos encabezados del CSV 
    #USE LOS DATOS OMO DICE EN EL EJEMPLO DE ARCHIVO FINAL
    game_data = {
        "nombre": name,
        "genero": genre,
        "desarrollador": developer,
        "clasificacion": esrb
    }
    return game_data


def save_games_to_csv(file_path, games_list):
    headers = ["nombre", "genero", "desarrollador", "clasificacion"]
    
    try:
        # newline='' es necesario en el módulo csv para evitar renglones vacíos extras en Windows
        with open(file_path, mode='w', encoding='utf-8', newline='') as csv_file:
            # Creamos el objeto escritor especializado en diccionarios
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            # 1. Escribimos la primera línea con los nombres de las columnas
            writer.writeheader()
            
            # 2. Escribimos todas las filas de videojuegos que recolectamos
            writer.writerows(games_list)
            
        print("\nSuccess: Data successfully saved to '{}'!".format(file_path))
        return True
    except IOError:
        print("\nError: Could not write to the file '{}'.".format(file_path))
        return False

def save_games_to_tsv(file_path, games_list):
    headers = ["nombre", "genero", "desarrollador", "clasificacion"]
    
    try:
        with open(file_path, mode='w', encoding='utf-8', newline='') as tsv_file:
            writer = csv.DictWriter(tsv_file, fieldnames=headers, delimiter='\t')
            writer.writeheader()
            writer.writerows(games_list)
        
        print("\nSuccess: Data successfully saved to '{}'!".format(file_path))
        return True
    except IOError:
        print("\nError: Could not write to the file '{}'.".format(file_path))
        return False

def run_video_game_manager():
    """Main orchestrator to handle the loop for N amount of video games."""
    print("Welcome to the Video Game Registry")
    all_games = []
    
    while True:
        # 1. Recolectamos la información del juego actual
        game = get_video_game_data()
        all_games.append(game)
        
        # 2. Preguntamos al usuario si desea continuar o detenerse
        decision = input("\nDo you want to add another game? (yes/no): ").strip().lower()
        if decision != 'yes' and decision != 'y':
            break
            
    # 3. Guardamos toda la lista recolectada en el archivo
    output_filename1 = "videogames.csv"
    # Guardamos el archivo con extensión .txt o .tsv para indicar que es de tabulaciones
    output_filename_csv = "videogames.csv"
    output_filename_tsv = "videogames.tsv"
    save_games_to_csv(output_filename_csv, all_games)
    save_games_to_tsv(output_filename_tsv, all_games)


if __name__ == "__main__":
    run_video_game_manager()


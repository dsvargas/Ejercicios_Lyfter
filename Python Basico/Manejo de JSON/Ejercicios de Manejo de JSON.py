# Investigue cómo leer y escribir archivos JSON en Python aquí.
#Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON (ipsum:lesson/python-basico/manejo-de-json)
## Debe leer el archivo para importar los Pokémones existentes.
## Luego debe pedir la información del Pokémon a agregar.
## Finalmente debe guardar el nuevo Pokémon en el archivo.
import json
def read_json(json_file_name):
    try:
        with open(json_file_name, 'r') as file:
            data = json.load(file)
        return data
    except:
        print("Error: Could not read the JSON file.")
        return None
    


def get_new_pokemon_info():
    try:
        
        # Pedir al usuario la información del nuevo Pokémon
        name = input("Enter the name of the Pokémon: ")
        type_ = input("Enter the type of the Pokémon: ")
        level = int(input("Enter the level of the Pokémon: "))
        weight = float(input("Weight in kg (e.g., 8.5): "))
        shiny_input = input("Is it Shiny? (yes/no): ").strip().lower()
        is_shiny = shiny_input in ['yes', 'y', 'si']
        item_input = input("Held Item (Press Enter if None): ").strip()
        held_item = item_input if item_input != "" else None

        #Sub-objeto/Diccionario Anidado (stats)
        print("\n--- Enter Pokémon Stats ---")
        hp = int(input("HP: "))
        attack = int(input("Attack: "))
        defense = int(input("Defense: "))
        sp_attack = int(input("Special Attack: "))
        sp_defense = int(input("Special Defense: "))
        speed = int(input("Speed: "))
        
        stats_dict = {
            "hp": hp,
            "attack": attack,
            "defense": defense,
            "sp_attack": sp_attack,
            "sp_defense": sp_defense,
            "speed": speed
        }
        # Crear un nuevo diccionario para el Pokémon
        new_pokemon = {
            "name": name,
            "type": type_,
            "level": level,
            "weight": weight,
            "shiny": is_shiny,
            "held_item": held_item,
            "stats": stats_dict
        }

        return new_pokemon

    except:
        print("Error: Could not add the new Pokémon to the JSON file.")

def save_json(json_file_name, data):
    try:
        with open(json_file_name, 'w') as file:
            json.dump(data, file, indent=4)
    except:
        print("Error: Could not write to the JSON file.")

def save_new_pokemon(json_file_name):
    # Leer los Pokémones existentes
    pokemons = read_json(json_file_name)
    if pokemons is None:
        pokemons = []  # Si no se pudo leer, iniciar con una lista vacía

    # Obtener la información del nuevo Pokémon
    new_pokemon = get_new_pokemon_info()
    if new_pokemon is not None:
        pokemons.append(new_pokemon)  # Agregar el nuevo Pokémon a la lista

        # Guardar la lista actualizada de Pokémones en el archivo JSON
        save_json(json_file_name, pokemons)
        print(f"{new_pokemon['name']} has been added to the Pokémon list.")
    else:
        print("Failed to add the new Pokémon.")
# Ejemplo de uso
save_new_pokemon('pokemons.json')
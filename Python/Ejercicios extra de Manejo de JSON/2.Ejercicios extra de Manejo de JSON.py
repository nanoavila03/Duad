#Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y::
#Lea el archivo JSON de Pokémon
#Pida al usuario un tipo de Pokémon
#Muestre todos los Pokémon que sean de ese tipo

import json

def read_pokemon_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        pokemon_data = json.load(file)
    return pokemon_data

def display_pokemon_by_type(pokemon_list, pokemon_type):
    found = False
    for pokemon in pokemon_list:
        types = pokemon.get('type', [])
        if pokemon_type.lower() in [t.lower() for t in types]:
            name = pokemon.get('name', {}).get('english', 'Unknown')
            print(f"Name: {name}, Type: {', '.join(types)}")
            found = True
    if not found:
        print(f"No Pokémon found of type: {pokemon_type}")


def ValidateTypeInput(pokemon_list, pokemon_type):
    all_types = set()
    for pokemon in pokemon_list:
        types = pokemon.get('type', [])
        for t in types:
            all_types.add(t.lower())  
    return pokemon_type.lower() in all_types 

def main():
    file_path = 'pokemon_data.json'
    pokemon_list = read_pokemon_json(file_path)
    pokemon_type = input("Enter a Pokémon type to search for: ").strip()
    while True:
        if ValidateTypeInput(pokemon_list, pokemon_type):
            break
        else:
            print("Invalid type. Please try again.")
            pokemon_type = input("Enter a Pokémon type to search for: ").strip()
    display_pokemon_by_type(pokemon_list, pokemon_type)


if __name__ == "__main__":
    main()
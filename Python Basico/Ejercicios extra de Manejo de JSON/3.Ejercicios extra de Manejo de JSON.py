#Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
#Lea el archivo JSON de Pokémon
#Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)

import json

def read_pokemon_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        pokemon_data = json.load(file)  
    return pokemon_data

def display_pokemon_stats(pokemon_list):
    for pokemon in pokemon_list:
        name = pokemon.get('name', {}).get('english', 'Unknown')
        base_stats = pokemon.get('base', {})
        print(f"Name: {name}")
        for stat, value in base_stats.items():
            print(f"{stat}: {value}")
        print()

def main():
    file_path = 'pokemon_data.json'  
    pokemon_list = read_pokemon_json(file_path)
    display_pokemon_stats(pokemon_list)

if __name__ == "__main__":
    main()
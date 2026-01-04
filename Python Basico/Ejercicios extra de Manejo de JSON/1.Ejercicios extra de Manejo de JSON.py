#Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
#Lea el archivo JSON de Pokémon
#Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel (o cualquier otro atributo definido)

import json

def read_pokemon_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        pokemon_data = json.load(file)
    return pokemon_data

def display_pokemon_info(pokemon_list):
    for pokemon in pokemon_list:
        name = pokemon.get('name', {}).get('english', 'Unknown')
        types = ', '.join(pokemon.get('type', []))
        base_stats = pokemon.get('base', {})
        hp = base_stats.get('HP', 'N/A')
        attack = base_stats.get('Attack', 'N/A')
        defense = base_stats.get('Defense', 'N/A')
        sp_attack = base_stats.get('Sp. Attack', 'N/A')
        sp_defense = base_stats.get('Sp. Defense', 'N/A')
        speed = base_stats.get('Speed', 'N/A')

        print(f"Name: {name}")
        print(f"Type: {types}")
        print(f"Base Stats: HP: {hp}, Attack: {attack}, Defense: {defense}, Sp. Attack: {sp_attack}, Sp. Defense: {sp_defense}, Speed: {speed}")
        print()

def main():
    file_path = 'pokemon_data.json' 
    pokemon_list = read_pokemon_json(file_path)
    display_pokemon_info(pokemon_list)

if __name__ == "__main__":
    main()

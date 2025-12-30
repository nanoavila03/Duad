#Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON (https://learning.lyfter.team/dashboard/roadmap/fffab4f1-5c3f-480a-9671-ae1a235c3b6a/dac6b243-2cab-496f-96de-5debb9ce613e)
#Debe leer el archivo para importar los Pokémones existentes.
#Luego debe pedir la información del Pokémon a agregar.
#Finalmente debe guardar el nuevo Pokémon en el archivo.

import json


def use_existing_file():
    filename = input("Enter the name of the existing JSON file (e.g., pokemon_data.json): ").strip()
    if not filename.endswith('.json'):
        filename += '.json'
    
    try:
        with open(filename, 'r') as file:
            json.load(file)
        print(f"Using existing file: {filename}")
        return filename
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        create_new = input("Do you want to create this file? (yes/no): ").strip().lower()
        if create_new in ['yes', 'y']:
            with open(filename, 'w') as file:
                json.dump([], file, indent=4, ensure_ascii=False)
            print(f"New file '{filename}' created successfully.")
            return filename
        else:
            return select_or_create_file()
    except json.JSONDecodeError:
        print(f"File '{filename}' is not a valid JSON file.")
        return select_or_create_file()


def create_new_file():
    filename = input("Enter the name for the new JSON file (e.g., my_pokemons.json): ").strip()
    if not filename.endswith('.json'):
        filename += '.json'
    
    try:
        with open(filename, 'r') as file:
            overwrite = input(f"File '{filename}' already exists. Overwrite? (yes/no): ").strip().lower()
            if overwrite in ['yes', 'y']:
                with open(filename, 'w') as file:
                    json.dump([], file, indent=4, ensure_ascii=False)
                print(f"File '{filename}' overwritten successfully.")
                return filename
            else:
                return select_or_create_file()
    except FileNotFoundError:
        with open(filename, 'w') as file:
            json.dump([], file, indent=4, ensure_ascii=False)
        print(f"New file '{filename}' created successfully.")
        return filename


def select_or_create_file():
    print("\n Pokémon JSON Manager ")
    print()
    print("1. Use existing JSON file")
    print("2. Create new JSON file")
    
    choice = validate_input("Select an option (1 or 2): ", int)
    
    if choice == 1:
        return use_existing_file()
    elif choice == 2:
        return create_new_file()
    else:
        print("Invalid option. Please select 1 or 2.")
        return select_or_create_file()


def add_pokemon(filename):
    with open(filename, 'r') as file:
        pokemons = json.load(file)

    name = input("\nEnter the Pokémon name: ")
    types = input("Enter the Pokémon types (separated by commas): ").split(',')
    
    hp = validate_input("Enter HP: ", int)
    attack = validate_input("Enter Attack: ", int)
    defense = validate_input("Enter Defense: ", int)
    sp_attack = validate_input("Enter Sp. Attack: ", int)
    sp_defense = validate_input("Enter Sp. Defense: ", int)
    speed = validate_input("Enter Speed: ", int)

    new_pokemon = {
        "name": {"english": name},
        "type": [t.strip().capitalize() for t in types],
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }

    pokemons.append(new_pokemon)

    with open(filename, 'w') as file:
        json.dump(pokemons, file, indent=4, ensure_ascii=False)
    print(f"\nPokémon {name} added successfully to {filename}.")


def validate_input(prompt, type_):
    while True:
        try:
            return type_(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid {type_.__name__}.")


def main():
    filename = select_or_create_file()
    
    while True:
        add_pokemon(filename)
        continue_adding = input("\nDo you want to add another Pokémon? (yes/no): ").strip().lower()
        if continue_adding not in ['yes', 'y']:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
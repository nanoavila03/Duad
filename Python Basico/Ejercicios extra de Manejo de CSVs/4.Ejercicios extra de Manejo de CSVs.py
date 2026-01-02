#Cree un programa que abra un archivo .csv con la información de videojuegos( en base al CSV que fue generado en el ejercicio 1) y:
#Lea el archivo .csv con videojuegos
#Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
#Muestre todos los videojuegos desarrollados por esa empresa en formato legible:

import csv

def filter_games_by_developer(file_path, developer):
    found_games = []
    
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if row['Developer'].strip().lower() == developer.lower():
                found_games.append(row)
    
    return found_games

def display_filtered_games(games, developer):
    if games:
        print(f"\nVideogames developed by '{developer}':")
        print()
        for game in games:
            print(f"Name: {game['Name']}")
            print(f"Genre: {game['Genre']}")
            print(f"Developer: {game['Developer']}")
            print(f"ESRB Rating: {game['ESRB Rating']}")
            print()
        print(f"\nTotal found: {len(games)} game(s)")
    else:
        print(f"\nNo games found developed by '{developer}'")

def validate_file(file_path):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            pass
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    return True

def main(): 
    file_path = "videogames.csv"
    if not validate_file(file_path):
        print("Please check the file and try again.")
        return
    developer_name = input("Enter the developer name to filter: ").strip()
    filtered_games = filter_games_by_developer(file_path, developer_name)
    display_filtered_games(filtered_games, developer_name)

if __name__ == "__main__":      
    main()
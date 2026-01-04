#Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
#Lea el archivo CSV de videojuegos
#Pida al usuario una clasificación ESRB (por ejemplo: "T")
#Muestre todos los videojuegos que tengan esa clasificación

import csv

def filter_games_by_rating(file_path, rating):
    
    found_games = []
    
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if row['ESRB Rating'].strip().upper() == rating.upper():
                found_games.append(row)
    
    return found_games

def display_filtered_games(games, rating):

    if games:
        print(f"\nVideogames with ESRB Rating '{rating}':")
        print()
        for game in games:
            print(f"Name: {game['Name']}")
            print(f"Genre: {game['Genre']}")
            print(f"Developer: {game['Developer']}")
            print(f"ESRB Rating: {game['ESRB Rating']}")
            print()
        print(f"\nTotal found: {len(games)} game(s)")
    else:
        print(f"\nNo games found with ESRB Rating '{rating}'")

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
    rating = input("Enter an ESRB Rating to filter by (e.g., E, T, M): ").strip()
    filtered_games = filter_games_by_rating(file_path, rating)
    display_filtered_games(filtered_games, rating)

if __name__ == "__main__":
    main()
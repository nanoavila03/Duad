#Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
#Lea el archivo .csv con videojuegos
#Cuente cuántos videojuegos hay de cada género
#Muestre el resultado de forma ordenada
import csv

def count_games_by_genre(file_path):
    genre_count = {}

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            genre = row['Genre'].strip()
            if genre in genre_count:
                genre_count[genre] += 1
            else:
                genre_count[genre] = 1

    return genre_count

def display_genre_counts(genre_count):
    print("Videogames count by genre:")
    print()
    for genre, count in sorted(genre_count.items()):
        print(f"{genre}: {count}")
    print()

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
    genre_count = count_games_by_genre(file_path)
    display_genre_counts(genre_count)

if __name__ == "__main__":
    main()
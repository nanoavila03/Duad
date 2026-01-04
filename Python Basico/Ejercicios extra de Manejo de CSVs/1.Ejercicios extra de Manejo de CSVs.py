#ree un programa que abra un archivo .csv con la información de videojuegos (el que fue generado en el ejercicio 1) y:
#Lea cada línea usando csv.reader()
#Muestre el contenido en pantalla de forma legible, línea por línea

import csv

headers = ["Title", "Developer", "Genre", "ESRB Rating"]

def open_and_display_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for header, value in zip(headers, row):
                print(f"{header}: {value}")
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

if __name__ == "__main__":
    file_path = "videogames.csv"
    if validate_file(file_path):
        open_and_display_csv(file_path)
    else:
        print("Please check the file and try again.")
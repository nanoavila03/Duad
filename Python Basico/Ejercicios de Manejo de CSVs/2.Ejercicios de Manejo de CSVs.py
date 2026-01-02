#Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.


import csv

videogames = []

videogames_headers = ['Name', 'Genre', 'Developer', 'ESRB Rating']

def add_videogame():
    name = input("Enter the name of the videogame: ")
    genre = input("Enter the genre of the videogame: ")
    developer = input("Enter the developer of the videogame: ")
    esrb_rating = input("Enter the ESRB rating of the videogame: ")
    
    videogame = {
        'Name': name,
        'Genre': genre,
        'Developer': developer,
        'ESRB Rating': esrb_rating
    }
    
    videogames.append(videogame)
    print(f"Videogame '{name}' added successfully!")

def save_to_tsv(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=videogames_headers, delimiter='\t')
        writer.writeheader()
        for game in videogames:
            writer.writerow(game)
    print(f"All videogames saved to '{filename}' successfully!")

def validate_n():
    while True:
        try:
            n = int(input("How many videogames do you want to add? "))
            if n > 0:
                return n
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    n = validate_n()
    for _ in range(n):
        add_videogame()
    save_to_tsv('videogames.csv')
if __name__ == "__main__":
    main()
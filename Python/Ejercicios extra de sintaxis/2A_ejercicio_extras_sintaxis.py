#Cree un diagrama de flujo que tenga un numero secreto del 1 al 10, y le pida al usuario adivinar ese número. El algoritmo no debe terminar hasta que el usuario adivine el numero.

import random

secret_number = random.randint(1, 10)
user_number = 0

user_number = int(input("Guess the secret number (between 1 and 10): "))

while not user_number == secret_number:
    print("Incorrect number, try again.")
    user_number = int(input("Guess the secret number (between 1 and 10): "))

print("Congratulations! You guessed the secret number.")
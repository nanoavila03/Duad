#Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
import random

secret_number = random.randint(1, 10)
# secret_number = 7  # For testing
guessed = False

while not guessed:
    entered_number = int(input("Guess the secret number (between 1 and 10): "))
    
    if entered_number == secret_number:
        print("You guessed the secret number!")
        guessed = True
        print("End of game")
    elif entered_number < secret_number: 
        print("Try again, the secret number is higher")
    else:
        print("Try again, the secret number is lower")
#Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
#1. Suma
#2. Resta
#3. Multiplicación
#4. División
#5. Borrar resultado
#Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
#Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.

def calculator():
    current_number = 0.0
    while True:
        print(f"Current number: {current_number}")
        print("Select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Clear result")

        choice = input("Enter the operation number you want to perform: ")

        if choice == '5':
            current_number = 0.0
            print("Result cleared.")
            continue

        try:
            new_number = float(input("Enter the number: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        if choice == '1':
            current_number += new_number
        elif choice == '2':
            current_number -= new_number
        elif choice == '3':
            current_number *= new_number
        elif choice == '4':
            if new_number == 0:
                print("Error: Cannot divide by zero.")
                continue
            current_number /= new_number
        else:
            print("Error: Invalid option. Please select a valid option.")
            continue    
        print(f"Result updated: {current_number}\n")
calculator()
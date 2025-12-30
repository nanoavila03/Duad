#Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
#1. Suma
#2. Resta
#3. Multiplicación
#4. División
#5. Borrar resultado
#Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
#Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.

def input_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Invalid number. Please enter a valid numeric value.")

def input_choice(prompt, choices):
    while True:
        choice = input(prompt)
        if choice in choices:
            return choice
        else:
            print("Error: Invalid choice. Please select a valid option.")

def show_menu():
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear Result")

def add(current_value, number):
    return current_value + number

def subtract(current_value, number):
    return current_value - number

def multiply(current_value, number):
    return current_value * number

def divide(current_value, number):
    if number == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return current_value / number

def clear_result():
    return 0.0

def execute_operation(choice, current_value, new_number):
    if choice == '1':
        return add(current_value, new_number)
    elif choice == '2':
        return subtract(current_value, new_number)
    elif choice == '3':
        return multiply(current_value, new_number)
    elif choice == '4':
        return divide(current_value, new_number)
    return current_value

def main():
    current_value = 0.0
    print(f"Current value: {current_value}")

    while True:
        if current_value == 0.0:
            print("Note: Current value is zero. You may want to add a number first.")
            current_value = input_number("Enter a number to start with: ")
            print(f"Current value: {current_value}")
        
        show_menu()
        choice = input_choice("Select an operation (1-5): ", ['1', '2', '3', '4', '5'])

        if choice == '5':
            current_value = clear_result()
            print(f"Result cleared. Current value: {current_value}")
            continue

        new_number = input_number("Enter a number: ")

        result = execute_operation(choice, current_value, new_number)
        
        if result is not None:
            current_value = result
            print(f"Current value: {current_value}")
        else:
            continue

if __name__ == "__main__":  
    main()
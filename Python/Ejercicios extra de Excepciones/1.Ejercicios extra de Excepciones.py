#Cree un programa que:
#Pida al usuario su nombre
#Si el nombre es numérico (isdigit()), haga raise ValueError("El nombre no puede ser un número")
#Luego pida su edad
#Si no es un número válido, capture el ValueError y muestre un mensaje
#Si todo sale bien, imprima un mensaje: "Hola <nombre>, su edad es <edad>"

def enter_name(prompt):
    name = input("Please enter your name: ")
    try:
        name = validate_name(name)
    except ValueError as ve:
        print(ve)
        return enter_name(prompt)
    return name 

def validate_name(name):
    if name.isdigit():
        raise ValueError("The name cannot be a number")
    return name

def enter_age(prompt):
    age = input("Please enter your age: ")
    try:
        age = validate_age(age)
    except ValueError as ve:
        print(ve)
        return enter_age(prompt)
    return age

def validate_age(age):
    try:
        age = int(age)
    except ValueError:
        raise ValueError("The age must be a valid number")
    return age

def main():
    name = enter_name("Enter your name: ")
    age = enter_age("Enter your age: ")
    print(f"Hello {name}, your age is {age}")

if __name__ == "__main__":
    main()
#Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

if (age < 3):
    print("Is a baby")
elif (age < 10):
    print("Is a child")
elif (age < 14):
    print("Is a preteen")
elif (age < 18):
    print("Is a teenager")
elif (age < 25):
    print("Is a young adult")
elif (age < 65):
    print("Is an adult")
else:
    print("Is a senior")
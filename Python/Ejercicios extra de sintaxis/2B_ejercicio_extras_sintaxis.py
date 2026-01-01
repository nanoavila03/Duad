#Cree un diagrama de flujo que pida 3 números al usuario. Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “Correcto”. Sino, mostrar “incorrecto”.

number1 = 0
number2 = 0
number3 = 0

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

sum_numbers = number1 + number2 + number3

if (number1 == 30):
    print("Correct!")
elif (sum_numbers == 30):
    print("Correct!")
else:
    print("Incorrect!")
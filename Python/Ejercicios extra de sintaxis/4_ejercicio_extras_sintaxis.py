#Tabla de multiplicar personalizada
#Pida al usuario un número del 1 al 10
#Muestre su tabla de multiplicar del 1 al 12

number = 0
number = int(input("Enter a number from 1 to 10 to see its multiplication table: "))
print(f'Multiplication table of {number}:')

for i in range(1, 13):
    result = number * i
    print(f'{number} x {i} = {result}')
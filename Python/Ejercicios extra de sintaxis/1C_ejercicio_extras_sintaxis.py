#Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado. Luego muestre el resultado de la suma.

entered_number = 0
total_sum = 0
ladder = ""

entered_number = int(input("Enter a number: "))

for i in range(1, entered_number + 1):
    total_sum += i
    
    if i < entered_number:
        ladder += str(i) + " + "
    else:
        ladder += str(i)

print(f'The sum of numbers from 1 to {entered_number} -> {total_sum} ({ladder})')
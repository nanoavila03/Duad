#Cree un programa que reciba una lista de números y calcule el promedio de los valores, luego cree una nueva lista con solo los valores mayores al promedio

my_list = []
for i in range(8):
    number = int(input("Enter a number: "))
    my_list.append(number)  
average = sum(my_list) / len(my_list)
above_average = []
for number in my_list:
    if number > average:
        above_average.append(number)
print(f"The average is: {average}")
print(f"Numbers above average: {above_average}")
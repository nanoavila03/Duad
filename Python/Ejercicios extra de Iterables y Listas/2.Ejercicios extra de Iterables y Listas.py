#Cree un programa que verifique si todos los elementos de una lista son positivos

my_list = []
for number in range(6):
    value = int(input("Enter a number: "))
    my_list.append(value)
number_positive = True
for number in my_list:
    if number < 0:
        number_positive = False
        break
if number_positive:
    print("All numbers are positive.")
else:
    print("There are negative numbers in the list.")
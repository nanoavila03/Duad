#Cree un programa que muestre el valor más pequeño de una lista sin usar min().

my_list = []
for value in range(5):
    number = int(input("Enter a number: "))
    my_list.append(number) 
min_value = my_list[0]
for number in my_list:
    if number < min_value:
        min_value = number
print(f"The smallest value in the list is: {min_value}")
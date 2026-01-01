#Cree un programa que cuente cuántas veces aparece un número específico en una lista. Pida al usuario una lista de números y otro número a buscar
my_list = []
search_number = 0

for list in range(10):
    number = int(input("Enter a number: "))
    my_list.append(number)
search_number = int(input("Enter the number to search for: "))
count = 0
for number in my_list:
    if number == search_number:
        count += 1 
print(f"The number {search_number} appears {count} times in the list.") 

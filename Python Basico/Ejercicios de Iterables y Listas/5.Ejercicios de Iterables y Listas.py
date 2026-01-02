#Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
numbers = []
user_number = 0

for number in range(10):
    user_number = int(input("Please enter a number: "))
    numbers.append(user_number)
print("The numbers you entered are:", numbers)
print("The highest number you entered is:", max(numbers))

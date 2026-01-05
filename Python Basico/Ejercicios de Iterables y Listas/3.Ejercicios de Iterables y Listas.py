#Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.


my_numbers = [10, 20, 30, 40, 50, 60 ,70 ,80 ,90 ,100,  110]

my_numbers[0], my_numbers[-1] = my_numbers[-1], my_numbers[0]  

print(my_numbers)

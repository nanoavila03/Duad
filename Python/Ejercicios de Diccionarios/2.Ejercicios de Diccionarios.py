#Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
#Ejemplos:
#list_a = [’first_name’, ‘last_name’, ‘role’]
#list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]
#→ {’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}


list_cars = ['brand', 'model', 'year']
list_values = ['Toyota', '4runner', 2006]
car_dict = {}

for i in range(len(list_cars)):
    car_dict[list_cars[i]] = list_values[i]
print("The car dictionary is:", car_dict)

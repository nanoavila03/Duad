#Cree un programa que use una lista para eliminar keys de un diccionario.
#Ejemplos:
#list_of_keys = [’access_level’, ‘age’]
#employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}
#→ {’name’: ‘John’, 'email’: ‘john@ecorp.com’}

data_dict = {
    'name': 'Mariano',
    'email': 'mariano12@mail.com',
    'access_level': 3,
    'age': 23
}       
keys_to_remove = ['access_level', 'age']    
for key in keys_to_remove:
    if key in data_dict:
        del data_dict[key]
print("The updated dictionary is:", data_dict)
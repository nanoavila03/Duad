#Cree una función convertir_a_entero(lista) que:
#Reciba una lista de strings
#Intente convertir cada elemento a entero usando int()
#Use try-except para atrapar los errores ValueError
#Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" y continuar con los demás

def convert_to_integer(list):
    integers = []
    for value in list:
        try:
            integer = int(value)
            integers.append(integer)
            print(f'"{value}" converted to {integer}')
        except ValueError:
            print(f"Could not convert the element: {value}")
    return integers

# Usage example
string_list = ["03", "Two", "10", "5.2", "Seven", "42"]
print("Result:")

if __name__ == "__main__":
    convert_to_integer(string_list)

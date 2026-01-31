#Cree una función sumar_valores(lista) que:
#Reciba una lista de elementos (strings, enteros, flotantes mezclados)
#Intente convertir cada elemento a tipo float
#Si puede, sume el valor y muestre: "<valor> sumado correctamente"
#Si no puede, muestre: "Elemento inválido: <valor>"
#Al final, imprima la suma total

def sum_values(list):
    total_sum = 0.0
    for value in list:
        try:
            number = float(value)
            total_sum += number
            print(f'"{value}" added successfully')
        except ValueError:
            print(f"Invalid element: {value}")
    print(f"Total sum: {total_sum}")
    return total_sum

my_list = ["10", "5.5", "abc", "20", "3.14", "xyz", "7"]
print("Result:")
if __name__ == "__main__":
    sum_values(my_list)
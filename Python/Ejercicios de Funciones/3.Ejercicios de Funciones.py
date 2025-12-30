#Cree una función que retorne la suma de todos los números de una lista.
#La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#[4, 6, 2, 29] → 41

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
result = sum_list([3,10,30, 2025])
print(result) 
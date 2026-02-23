#Considere los siguientes dos algoritmos:

def linear_search(my_list, target):
    for item in my_list:
        if item == target:
            return True
    return False

def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1  #Error corregido: era 'lst'
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

#Preguntas:
#¿Cuál es la complejidad de cada algoritmo?
# Linear Search: O(n) - recorre todos los elementos
# Binary Search: O(log n) - divide la lista a la mitad cada vez

#¿En qué condiciones conviene usar cada uno?
# Linear Search: listas pequeñas o no ordenadas, una sola búsqueda
# Binary Search: listas grandes Y ordenadas, múltiples búsquedas

#¿Qué pasa si la lista no está ordenada?
# Linear Search: funciona normal
# Binary Search: NO funciona, da resultados incorrectos (requiere lista ordenada)
#Crea un bubble_sort por tu cuenta sin revisar el código de la lección.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def main():
    List = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", List)
    sorted_list = bubble_sort(List.copy())
    print("Sorted list (ascending):", sorted_list)
    sorted_list_descending = bubble_sort_descending(List.copy())
    print("Sorted list (descending):", sorted_list_descending)

if __name__ == "__main__":
    main()
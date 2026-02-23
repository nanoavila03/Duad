def bubble_sort(lst):
    if not isinstance(lst, list):
        raise TypeError("El parámetro debe ser una lista")
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

if __name__ == "__main__":
    print(bubble_sort([1, 2, 3, 4, 5])) 
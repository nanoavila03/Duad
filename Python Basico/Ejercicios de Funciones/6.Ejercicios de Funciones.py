#Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#“python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def sort_hyphenated_string(hyphenated_string):
    words_list = hyphenated_string.split('-')
    words_list.sort()
    sorted_string = '-'.join(words_list)
    return sorted_string
result = sort_hyphenated_string("KTM-Husqvarna-Yamaha-Suzuki-Honda")
print(result)

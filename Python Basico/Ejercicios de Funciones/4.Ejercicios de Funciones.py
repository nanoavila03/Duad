#Cree una función que le de la vuelta a un string y lo retorne.
#Esto ya lo hicimos en iterables.
#“Hola mundo” → “odnum aloH”

def reverse_string(s):
    return s[::-1]  
result = reverse_string("Pura Vida Costa Rica")
print(result)
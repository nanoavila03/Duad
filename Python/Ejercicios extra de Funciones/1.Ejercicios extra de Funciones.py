#Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto

def count_character(text, character):
    count = 0
    for char in text:
        if char == character:
            count += 1
    return count

text = "Hi how do you do?"  
character = "o"
result = count_character(text, character)
print (f"The character '{character}' appears {result} times in the text.") 
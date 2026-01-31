#Cree una función que reciba un string y retorne cuántas vocales contiene

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
text = "Hello, welcome to the world of Python programming!"
result = count_vowels(text)
print(f"The text contains {result} vowels.")
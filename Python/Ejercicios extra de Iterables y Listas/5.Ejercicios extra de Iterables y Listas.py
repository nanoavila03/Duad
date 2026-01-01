#Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras

my_words = []
for i in range(5):
    word = input("Enter a word: ")
    my_words.append(word)   
long_words = []
for word in my_words:
    if len(word) > 4:
        long_words.append(word)
print(f"Words with more than 4 letters: {long_words}")
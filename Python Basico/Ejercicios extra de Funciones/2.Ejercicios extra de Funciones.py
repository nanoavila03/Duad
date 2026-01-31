#Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras

def filter_words_by_length(words, n):
    filtered_words = []
    for word in words:
        if len(word) > n:
            filtered_words.append(word)
    return filtered_words
words = ["apple", "banana", "kiwi", "cherry", "pineapple", "grape"]
n = 5
result = filter_words_by_length(words, n)
print(f"Words with more than {n} letters: {result}")
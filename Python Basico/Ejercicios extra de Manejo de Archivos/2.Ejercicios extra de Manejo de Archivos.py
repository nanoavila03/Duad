#Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.

def create_file_from_input(filename):
    print("Enter a message (type 'END' to finish):")
    lines = ""
    while True:
        line = input("\nEnter message: ")
        if line.lower() == 'end':
            break
        if line:
            lines += line + "\n"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(lines)
    print(f"File '{filename}' created with the provided message.")
    return lines

def count_words_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()   
    words = content.split()
    word_count = len(words) 
    print(f"The file '{filename}' contains {word_count} words.")
    return word_count

def main():
    filename = 'Text_for_counting.txt'
    create_file_from_input(filename)
    count_words_in_file(filename)
    print("\nProcess completed.")

if __name__ == "__main__":
    main()
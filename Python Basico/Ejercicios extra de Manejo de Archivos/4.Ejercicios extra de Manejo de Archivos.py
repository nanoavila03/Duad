#Cree un programa que:
#Pida al usuario una línea de texto
#Agregue esa línea al final de un archivo existente
#Si el archivo no existe, lo crea automáticamente

def create_file_from_input(filename):
    print("Enter text lines (type 'END' to finish):")
    lines = []

    while True:
        line = input("\nEnter line: ")
        if line.lower() == 'end':
            break
        if line:
            lines.append(line)

    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line + '\n')
    
    print(f"File '{filename}' created with the provided lines.")
    return lines

def append_line_to_file(filename):
    while True:
        line_to_append = input("\nEnter a line to append to the file: ")
        if line_to_append:
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(line_to_append + '\n')
            print(f"Line appended to '{filename}'.")
            break
        else:
            print("Please enter a valid line.")


def main():
    filename = 'Appended_text.txt'
    
    choice = input("Do you want to create a new file? (yes/no): ")
    
    if choice.lower() == 'yes':
        create_file_from_input(filename)
    while True:
        if input("Do you want to append a line to the file? (yes/no): ").lower() != 'yes':
            break   
        append_line_to_file(filename)
        print("\nProcess completed.")
    
    with open(filename, 'r', encoding='utf-8') as file:
        print(f'\nThe content of the file is:\n{file.read()}')

if __name__ == "__main__":
    main()


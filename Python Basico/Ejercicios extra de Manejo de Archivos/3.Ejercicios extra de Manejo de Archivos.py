#Cree un programa que:
#Lea un archivo línea por línea
#Convierta cada línea a mayúsculas
#Escriba el contenido en un nuevo archivo


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

def convert_file_to_uppercase(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    with open(output_filename, 'w', encoding='utf-8') as outfile:
        for line in lines:
            outfile.write(line.upper())

    print(f"Content from '{input_filename}' converted to uppercase and written to '{output_filename}'.")
    return [line.upper() for line in lines]

def main(): 
    input_filename = 'Original_text.txt'
    output_filename = 'Uppercase_text.txt'
    
    create_file_from_input(input_filename)
    convert_file_to_uppercase(input_filename, output_filename)
    print("\nProcess completed.")
    with open(output_filename, 'r', encoding='utf-8') as file:
        print(f'\nThe uppercase content is:\n{file.read()}')

if __name__ == "__main__":
    main()
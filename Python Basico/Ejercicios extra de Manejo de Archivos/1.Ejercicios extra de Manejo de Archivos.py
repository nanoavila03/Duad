#Cree un programa que lea un archivo con texto línea por línea, quite los saltos de línea (\n) y escriba todo el contenido en un solo renglón en un nuevo archivo

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

def read_file_to_single_line(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    
    single_line = ' '.join(line.strip() for line in lines)
    
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        outfile.write(single_line)
    
    print(f"Content from '{input_filename}' written to '{output_filename}' in a single line.")
    return single_line

def main():
    input_filename = 'New_text.txt'
    output_filename = 'New_Message.txt'
    
    create_file_from_input(input_filename)
    read_file_to_single_line(input_filename, output_filename)
    print("\nProcess completed.")
    with open(output_filename, 'r', encoding='utf-8') as file:
        print(f'\nThe message is: {file.read()}')

if __name__ == "__main__":
    main()

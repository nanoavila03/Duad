#Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def read_songs(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        songs = file.readlines()
    return [song.strip() for song in songs if song.strip()]


def write_songs(output_file, songs):
    with open(output_file, 'w', encoding='utf-8') as file:
        for song in songs:
            file.write(song + '\n')


def sort_songs(songs):
    return sorted(songs, key=str.lower)


def main():
    input_file = "songs.txt"
    output_file = "songs_sorted.txt"
    
    songs = read_songs(input_file)
    sorted_songs = sort_songs(songs)
    write_songs(output_file, sorted_songs)
    
    print(f"Sorted {len(sorted_songs)} songs successfully!")


if __name__ == "__main__":
    main()
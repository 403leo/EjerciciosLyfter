# Codigo para leer el texto de canciones de un archivo txt
def read_songs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        songs = file.readlines()
    return songs

# Metodo que ordena las canciones y las devuelve
def sort_songs(songs):
    return sorted(songs)

# Metodo para agrrar las canciones del txt, los ordene alfabeticamente y lo guarde en un nuevo archivo txt
def save_sorted_song_list_to_file(songs):
    # Ordenar las canciones alfabeticamente del canciones.txt con el metodo de sorted() 
    # y guardarlas en un nuevo archivo txt llamado canciones_ordenadas.txt


    # Llama un metodo que ordene las canciones y las devuelva
    sorted_songs = sort_songs(songs)
    with open('canciones_ordenadas.txt', 'w', encoding='utf-8') as file:
        for song in sorted_songs:
            file.write(song.strip() + '\n')

# llamar al metodo para pasar la lista de canciones a un archivo con las canciones ordenadas
songs = read_songs('canciones.txt')
save_sorted_song_list_to_file(songs)
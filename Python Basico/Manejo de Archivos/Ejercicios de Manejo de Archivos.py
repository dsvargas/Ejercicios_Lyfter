#Ejercicios de Manejo de Archivos
#1 Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.
# 

def read_complete_file():
    # Usamos 'with' para un manejo seguro del archivo
    with open('songs.txt', 'r', encoding='utf-8') as file:
        #Cambiar de  .read() to .readlines() to get a list
        content = file.readlines()
    return  content 

def sort_songs_file():
    song_list = read_complete_file()
    song_list.sort()

    with open("sorted_songs.txt", "w") as output_file:
            # Recorremos la lista ya ordenada y escribimos cada canción en el nuevo archivo
            for song in song_list:
                output_file.write(song)

sort_songs_file()
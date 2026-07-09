def filter_songs_alphabethically(path): #Parámetro y variable path
    with open(path , "r", encoding="utf-8") as file: # 'r' for read utf-8 para incluir caracteres en español / Con el path como file:
        content = file.read() #Leer el contenido del file.
        content =  content.split("\n") #Divide el contenido en una lista separada por saltos de línea.
        content = [line for line in content if line.strip() != ""] #Para esta línea , investigué puesto que el output del archivo 2 tenía 13 líneas en blanco las cuales eliminé con este comando.
        sorted_songs = sorted(content) #Con este comando ordeno el contenido de A-Z

    with open("SortedSongs.txt", "w", encoding="utf-8") as output_file: #Con el archivo como output
        for song in sorted_songs: #Por cada canción ordenada en sorted_songs
            output_file.write(song + "\n") #Crear un archivo nuevo con las canciones, separadas por un salto de línea.

filter_songs_alphabethically('Manejo de Archivos/Songs.txt') #Llamamos a la función y damos los datos al parámetro

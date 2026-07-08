import csv

def open_csv_file(path): #Abre el archivo
    file = open(path, 'r', encoding="utf-8")
    return file


def read_csv_file(file): #Lee el archivo
    reader = csv.reader(file)
    return reader


def genre_counter(counter, genre): #Contador de género
    if genre in counter: #Si el género está en el contador
        counter[genre] += 1 #Agregarle 1 a ese género
    else:
        counter[genre] = 1 #Sino, el contador va a ser 1


def filter_rows(reader, counter): #Iteración de los rows
    next(reader) # Saltar el encabezado
    for row in reader: #Por cada row en el archivo
        genre_counter(counter, row[1]) #Llamamos a la función genre_counter, preguntamos el género, y cuántos hay en el row [1] (Género)


def show_genres(counter): # Mostrar los géneros
    print("Generos encontrados:\n") 
    for genre in counter: # Por cada género en el contador:
        print(f"{genre}: {counter[genre]}") #Imprimir el Género, y el conteo de cuántos hay de ese género


def main():
    open_file = open_csv_file("Manejo de CSVs/Lista_de_videojuegos.csv") #Llamamos a la función open_csv_file y la guardamos en una variable
    read = read_csv_file(open_file) #Llamamos la función read_csv_file con el parámetro guardado en la variable open_file
    genre_cnt = {} #Diccionario vacío, aquí se van a guardar tanto el contador como el género
    filter_rows(read, genre_cnt) # Acá vamos a filtrar el género del archivo
    show_genres(genre_cnt) # Por último, mostrar el resultado
    open_file.close() # Cerrar el archivo
main()
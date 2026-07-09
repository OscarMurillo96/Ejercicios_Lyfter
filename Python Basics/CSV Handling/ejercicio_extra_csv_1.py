import csv

def open_csv_file(path): #Abre el archivo
    file = open(path, 'r', encoding="utf-8")
    return file


def read_csv_file(file): #Lee el archivo
    reader = csv.reader(file)
    return reader


def iterate_each_row(reader): #Itera el archivo
    next(reader) #Salta el encabnezado o header
    for row in reader: #Por cada row en el archivo reader
        print(f"Nombre: {row[0]}") #Como es una lista, vamos a acceder a sus valores vía índice [0]
        print(f"Género: {row[1]}") #Como es una lista, vamos a acceder a sus valores vía índice [1]
        print(f"Desarrollador: {row[2]}") #Como es una lista, vamos a acceder a sus valores vía índice [2]
        print(f"Clasificación: {row[3]}") #Como es una lista, vamos a acceder a sus valores vía índice [3]
        print("") #Imprime una linea vacía para separar y que sea visiblmente más legible.


def main():
    open_file = open_csv_file("Manejo de CSVs/Lista_de_videojuegos.csv") #Llamamos a la función open_csv_file y la guardamos en una variable
    read = read_csv_file(open_file) #Llamamos la función read_csv_file con el parámetro guardado en la variable open_file
    iterate_each_row(read) 
    open_file.close() # Cerrar el archivo
main()

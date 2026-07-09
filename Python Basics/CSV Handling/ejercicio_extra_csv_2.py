import csv

def open_csv_file(path): #Abre el archivo
    file = open(path, 'r', encoding="utf-8")
    return file


def read_csv_file(file): #Lee el archivo
    reader = csv.reader(file)
    return reader


def request_classification(): #Pide la clasificación
    while True:
        try:
            classification = input("Digite la clasificación que desea consultar: ")
            if classification not in ["E", "E10+", "T", "M", "AO", "RP"]: #Si la clasificación no se encuentra entre estas opciones
                raise ValueError #Levantar un error de valor
            return classification #Nos da el valor que vamos a consultar
        except ValueError as error:
            print(error)


def show_classification(reader, classification):
    next(reader)
    for row in reader:
        if row[3] == classification:
            print(f"Nombre: {row[0]}") #Como es una lista, vamos a acceder a sus valores vía índice [0]
            print(f"Género: {row[1]}") #Como es una lista, vamos a acceder a sus valores vía índice [1]
            print(f"Desarrollador: {row[2]}") #Como es una lista, vamos a acceder a sus valores vía índice [2]
            print(f"Clasificación: {row[3]}") #Como es una lista, vamos a acceder a sus valores vía índice [3]
            print("") #Imprime una linea vacía para separar y que sea visiblmente más legible.


def main():
    open_file = open_csv_file("Manejo de CSVs/Lista_de_videojuegos.csv") #Llamamos a la función open_csv_file y la guardamos en una variable
    read_file = read_csv_file(open_file) #Llamamos la función read_csv_file con el parámetro guardado en la variable open_file
    request_class = request_classification() #Llamamos a la función request_classification, y guardamos el resultado en una variable
    show_classification(read_file, request_class) #Llamamos a la función show_classification, y va a contener el archivo, y la clasificación ingresada
    open_file.close() # Cerrar el archivo
main()

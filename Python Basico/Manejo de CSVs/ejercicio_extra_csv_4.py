import csv

def open_csv_file(path): #Abre el archivo
    file = open(path, 'r', encoding="utf-8")
    return file


def read_csv_file(file): #Lee el archivo
    reader = csv.reader(file)
    return reader


def request_developer(): #Pide el desarrollador
    while True: 
        try:
            developer = input("Ingrese el nombre del desarrollador: ")
            if developer == "": #Si el input se envía vacío
                raise ValueError # Levantar un error
            return developer #Retornar el resultado
        except ValueError as error:
            print(error)


def filter_developer(reader, developer): # Filtrar el desarrollador
    next(reader) # Saltar el encabezado
    print(f"Videojuegos desarrollados por: {developer}") 
    found = False #Bandera iniciada en False
    for row in reader: #Por cada row en el archivo
        if row[2] == developer: #Si el row[2] (Desarrollador) coincide con la búsqueda del usuario:
            print(f"- {row[0]} (Clasificación: {row[3]}, Género: {row[1]})") #Imprimir el formato solicitado
            found = True #Cambiar la bandera a True
    if found == False: # Si la bandera queda en False:
        print("Desarrollador no encontrado.") # Imprimir un custom message de no encontrado


def main():
    open_file = open_csv_file("Manejo de CSVs/Lista_de_videojuegos.csv") #Llamamos a la función open_csv_file y la guardamos en una variable
    read = read_csv_file(open_file) #Llamamos la función read_csv_file con el parámetro guardado en la variable open_file
    dev = request_developer() #Llamar a la función request_developer
    filter_developer(read, dev) #Llamar a la función filter_developer y pasarle los parámetros de lectura del archivo, y el desarrollador que ingresó el usuario
    open_file.close()  # Cerrar el archivo
main()
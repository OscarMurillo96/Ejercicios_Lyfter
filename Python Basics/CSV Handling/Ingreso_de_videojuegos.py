import csv

def request_game_name():
    gamename = input("Ingrese el nombre del videojuego: ")
    if gamename == "":
        raise ValueError("El nombre del videojuego no puede estar vacío.")
    return gamename #Retornar el valor de gamename.


def request_game_genre():
    gamegenre = input("Ingrese el género del videojuego: ")
    if gamegenre == "":
        raise ValueError("El género del videojuego no puede estar vacío.")
    return gamegenre #Retornar el valor de gamegenre.


def request_game_developer():
    gamedev = input("Ingrese el desarrollador del videojuego: ")
    if gamedev == "":
        raise ValueError("El desarrollador del videojuego no puede estar vacío.")
    return gamedev #Retornar el valor de gamedev.


def request_game_clasification():
    while True:
        try:
            gameclass = input("Ingrese la clasificación del videojuego: ")
            if gameclass == "":
                raise ValueError("La clasificación del videojuego no puede estar vacía.")
            if gameclass not in ["E", "E10+", "T", "M", "AO", "RP"]:
                raise ValueError("La clasificación debe ser E, E10+, T, M, AO, RP")
            return gameclass #Retornar el valor de gameclass.
        except ValueError as error:
            print(error)


def request_game():
    my_game_list = [] #Lista vacía para guardar los valores
    while True:
        try:
            quantity = int(input("Cuántos videojuegos desea ingresar: ")) #Cantidad de juegos que van a ser ingresados
            for i in range(quantity): #Por cada i en el rango de quantity
                name = request_game_name() #Llamamos a la función request_game_name y guardamos su resultado en la variable name.
                genre = request_game_genre() #Llamamos a la función request_game_genre y guardamos su resultado en la variable name.
                dev = request_game_developer() #Llamamos a la función request_game_developer y guardamos su resultado en la variable name.
                classification = request_game_clasification() #Llamamos a la función request_game_clasification y guardamos su resultado en la variable name.
                my_game_list.append([name, genre, dev, classification]) #Añadimos el valor guardado en las variables en la lista vacía.
            return my_game_list #Retornamos la lista
        except ValueError as error:
            print(f"Cantidad incorrecta. Detalles: {error}")


def save_to_csv(path, data): #Path y data como parámetros
    with open(path, 'w', encoding="utf-8", newline='') as file: #Con el archivo definido en path abierto como file:
        writer = csv.writer(file) #Writer va a llamar a el objeto csv.writer y va a escribir en el archivo.
        writer.writerow(["Nombre", "Género", "Desarrollador", "Clasificación"]) #writerow va a escribir este row al inicio del archivo, que van a dar nombre a las celdas.
        writer.writerows(data) #writerows va a escribir los datos que le pasemos a la función request_game


def main():
    name = request_game() #name va a almacenar los datos que vamos a pasar a data
    save_to_csv("Manejo de CSVs/Lista_de_videojuegos.csv", name) #path y data en ese orden, llamamos a la función save_to_csv
main()
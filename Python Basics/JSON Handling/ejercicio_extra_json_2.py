import json


def read_json(path): #Parámetro path
    with open(path, 'r', encoding="utf-8") as file: #Con el archivo en modo lectura como file:
        pokemons = json.load(file) #pokemons es igual a json.load(file), lo cual abre el archivo
        return pokemons #Retornar el contenido


def request_data(pokemons): #Recibe pokemons
    found = False #Bandera inicializada en False
    user_search = input("Ingrese el tipo de Pokémon que desea consultar: ") #Búsqueda del usuario
    for pokemon in pokemons: #Por cada pokemon en pokemons
        if user_search.lower() == pokemon["type"].lower(): #si la búsqueda del usuario (convertir a lower) coincide con el tipo en el archivo json (convertir a lower)
            print(f"Pokémons de tipo {user_search}: {pokemon["name"]}") #Imprime un custom message, más el tipo de pokémon realizado en la búsqueda
            found = True #Cambiamos la bandera a True
    if not found: #Si no encuentra
        print("No se encontraron pokémons de este tipo, vuelve a intentarlo.") #Custom message


if __name__ == "__main__":
    read = read_json("Manejo de JSON/Pokémons.json") #Llama a la función read_json()
    request_data(read) #Llama a la función request_data()
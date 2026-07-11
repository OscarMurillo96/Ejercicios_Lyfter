import json


def read_json(path): #Parámetro path
    with open(path, 'r', encoding="utf-8") as file: #Con el archivo en modo lectura como file:
        pokemons = json.load(file) #pokemons es igual a json.load(file), lo cual abre el archivo
        return pokemons #Retornar el contenido


def iterate_json(pokemons): #Recibe pokemons
    for pokemon in pokemons: #Por cada pokémon en pokémons
        print(f"Nombre: {pokemon["name"]} | Tipo: {pokemon["type"]} | Nivel: {pokemon["level"]}") #Imprimir string + key 


if __name__ == "__main__":
    read = read_json("Manejo de JSON/Pokémons.json") #Llama a la función read_json()
    iterate_json(read) #Llama a la función iterate_json()
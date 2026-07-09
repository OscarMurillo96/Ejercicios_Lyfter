import json


def read_json(path): #Parámetro path
    with open(path, 'r', encoding="utf-8") as file: #Con el archivo en modo lectura como file:
        pokemons = json.load(file) #pokemons es igual a json.load(file), lo cual abre el archivo
        return pokemons #Retornar el contenido


def filter_stats(pokemons):  #Recibe pokemons
    for pokemon in pokemons: #Por cada pokémon dentro de pokemons
        print(f"Nombre: {pokemon["name"]}") #Busca el key name
        print(f"Ataque: {pokemon["stats"]["attack"]}") #Busca el key attack del diccionario anidado stats y retorna su valor.
        print(f"Defensa: {pokemon["stats"]["defense"]}") #Busca el key defense del diccionario anidado stats y retorna su valor.
        print(f"Velocidad: {pokemon["stats"]["speed"]}\n") #Busca el key speed del diccionario anidado stats y retorna su valor.


if __name__ == "__main__":
    read = read_json("Manejo de JSON/Pokémons.json") #Llama a la función read_json()
    filter_stats(read) #Llama a la función filter_stats()
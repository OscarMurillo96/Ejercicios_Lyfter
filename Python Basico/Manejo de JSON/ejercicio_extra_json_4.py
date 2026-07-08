import json


def read_json(path): #Parámetro path
    with open(path, 'r', encoding="utf-8") as file: #Con el archivo en modo lectura como file:
        pokemons = json.load(file) #pokemons es igual a json.load(file), lo cual abre el archivo
        return pokemons #Retornar el contenido


def group_type(pokemons): # Recibe pokemons
    empty_dict = {} #Diccionario vacío
    for pokemon in pokemons: #Por cada pokemon en pokemons
        if pokemon["type"] in empty_dict: #Si el tipo de pokémon ya está dentro del diccionario
            empty_dict[pokemon["type"]].append(pokemon["level"]) #Añade el nivel al diccionario vacío para cada tipo
        else:
            empty_dict[pokemon["type"]] = [pokemon["level"]] #Si el tipo no existe, se crea y se le asigna un nivel.
    return empty_dict


def calculate_average(empty_dict):
    for pokemon, levels in empty_dict.items(): #Por cada item, guarda la llave en pokemon, y el valor en levels
        average = round(sum(levels) / len(levels), 2) #Promedio es igual a la suma de los niveles dividido entre los niveles
        print(f"Tipo: {pokemon} -> Promedio de nivel: {average}")


if __name__ == "__main__":
    read = read_json("Manejo de JSON/Pokémons.json") #Llama a la función read_json()
    group =  group_type(read) #Llama a la función group_type()
    calculate_average(group) #Llama a la función calculate_average()
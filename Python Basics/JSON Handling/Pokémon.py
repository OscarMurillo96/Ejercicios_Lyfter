import json


def read_json(path): #Parámetro path
    with open(path, 'r', encoding="utf-8") as file: #Con el archivo en modo lectura como file:
        pokemons = json.load(file) #pokemons es igual a json.load(file), lo cual abre el archivo
        return pokemons #Retornar el contenido


def request_data():
    pokemon = {} #Diccionario vacío
    pokemon["name"] = input("Ingrese el nombre del Pokémon: ") #Campo nombre del diccionario.
    pokemon["type"] = input("Ingrese el tipo del Pokémon: ") #Campo tipo del diccionario.
    pokemon["level"] = exception_handling("Ingrese el nivel del Pokémon: ", int) #Campo nivel del diccionario.
    pokemon["weight_kg"] = exception_handling("Ingrese el peso del Pokémon: ", float) #Campo peso del diccionario.
    pokemon["is_shiny"] = input("Es shiny?: ") #Campo shiny del diccionario.
    if pokemon["is_shiny"].lower() == "si": #Convertimos a lowercase, si el pokémon es shiny, entonces:
        pokemon["is_shiny"] = True # El valor de shiny es True
    elif pokemon["is_shiny"].lower() == "no": #Convertimos a lowercase, si el pokémon no es shiny, entonces:
        pokemon["is_shiny"] = False # El valor de shiny es False
    pokemon["held_item"] = input("nombre del held item?: ") #Ingresar el nombre del held item
    if pokemon["held_item"] == "": # Si no tiene held item o el campo queda vacío
        pokemon["held_item"] = None # El valor de held item va a ser None
    counter = 1 #Contador inicializado en 1
    my_list = [] #Lista vacía
    number_skills = exception_handling("Ingrese el número de skills que desea agregar: ", int) #Pregunta al usuario cuantas skills desea ingresar
    while counter <= number_skills: #Ingresa al loop
        p_skills = input("Skill: ") #Ingreso de skill individual
        my_list.append(p_skills) #Agrega cada skill a my_list
        counter += 1  #Suma 1 al contador
    pokemon["skills"] = my_list #Agrega los valores de my_list a el dict de skills
    p_stats = {} #Diccionario vacío
    p_stats["hp"] = exception_handling("Hp: ", int) #Campo hp del diccionario.
    p_stats["attack"] = exception_handling("Attack: ", int) #Campo attack del diccionario.
    p_stats["defense"] = exception_handling("Defense: ", int) #Campo defense del diccionario.
    p_stats["sp_attack"] = exception_handling("SP Attack: ", int) #Campo sp_attack del diccionario.
    p_stats["sp_defense"] = exception_handling("SP Defense: ", int) #Campo sp_defense del diccionario.
    p_stats["speed"] = exception_handling("Speed: ", int) #Campo speed del diccionario.
    pokemon["stats"] = p_stats #Agrega los valores del diccionario p_stats al diccionario stats
    return pokemon #Retornar pokémon


def exception_handling(custom_message, conversion): #Handling de errores de input
    while True: #Mientras sea verdadero
        try: #Intentar
            user_result = conversion(input(custom_message)) #user_result va a ser igual a la conversión del input con el valor custom_message
            return user_result #Retornar user_result
        except ValueError as error: # Exception
            print(f"Valor inválido. Detalles: {error}") #Custom message


def new_pokemon(path, pokemon): #Path y recibe el pokemon generado anteriormente
    with open(path, 'w', encoding="utf-8") as file: #Método de escritura en archivo.
        json.dump(pokemon, file, indent=4) #Método de salida del archivo


if __name__ == "__main__":
    read = read_json("Manejo de JSON/Pokémons.json") #Lee el archivo JSON
    request = request_data() #Llama a la función que pide los datos
    read.append(request) #Añade el pokémon a la lista del JSON
    new_pokemon("Manejo de JSON/Pokémons.json", read) #Edita el archivo JSON con el nuevo pokémon


#No sé mucho de Pokémons, nunca ví la serie, pero disfruté bastante haciendo el programa 🎉

# "Todo el mundo toma un camino equivocado de vez en cuando. Sigue adelante y no podrás equivocarte" ---Ash Ketchum---
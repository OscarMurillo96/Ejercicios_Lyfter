def return_words(my_list, my_number): #Parámetro
    new_list = [] #Lista vacía
    for word in my_list: #Por cada palabra (word) en my_list
        if len(word) > my_number: #Si cada palabra es mayor al número de entrada de my_number
            new_list.append(word) # Añadimos esa palabra a la nueva lista (new_list)

    return new_list # Retorno new_list

print(return_words(["cielo", "sol", "maravilloso", "dia"], int(input("Digite el numero minimo de letras: ")))) #Print a la lista, y output de los parámetros.


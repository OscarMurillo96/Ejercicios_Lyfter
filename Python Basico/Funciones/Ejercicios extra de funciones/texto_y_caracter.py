def receive_text_and_character(my_text, my_character): #Parámetros a usar
    counter = 0 #Contador para saber cuantas veces aparece el cáracter dentro del texto
    for text in my_text: #Por cada text (letra) en my_text
        if my_character == text: #Si, el cáracter buscado coincide con un cáracter del recorrido
            counter += 1 #Sumamos 1 al contador
    print(f"El caracter buscado aparece {counter} veces dentro del texto") #Print a la solución

receive_text_and_character(input("Ingrese cualquier texto: "), input("Ingrese un cáracter a buscar: ")) #Output de los parámetros

def add_values_and_sum(my_list): #Lista como parámetro
    total = 0 #Total para hacer la suma
    for item in my_list: #Por cada ítem de mi lista:
        try: #Si sigue un happy path, va a seguir esta lógica.
            converted = float(item) #Convertir los ítems en flotante
            print(f"{converted} sumado correctamente") #Cada ítem que se pudo sumar
            total += converted #Lo agregamos a total
        except ValueError: #Si sigue un unhappy path va a seguir esta lógica.
            print(f"Elemento inválido: {item}") #Imprime el ítem que no se pudo convertir, ni sumar

    print(f"Total de la suma: {total}") #El total de toda la sema de los ítems que sí se pudieron sumar

add_values_and_sum(['10','manzana','5.5','3', 'n/a']) #Llamamos a la función y definimos los datos del parámetro.

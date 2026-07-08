def convert_to_int(my_list): #my_list como parámetro.
    for item in my_list: #Por cada ítem de mi lista
        try: #Vamos a intentar 
            converted = int(item) #Convertir cada uno de esos ítems a integer
            print(f"\n{item} convertido a {converted}\n") #En caso de ser correcto, se imprime este mensaje
        except ValueError: #En caso de no poderse.
            print(f"No se pudo convertir el elemento: {item}\n") #Se imprime este otro mensaje con el ítem que no se pudo convertir.

convert_to_int(['4', 'hola', '10', '5.2']) #Llamar a la función con los datos del parámetro
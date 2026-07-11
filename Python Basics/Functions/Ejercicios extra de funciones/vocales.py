def return_vocals(my_string): #Parámetro
    counter = 0 #Contador
    vocals = ["a", "e", "i", "o", "u"] #Vocales definidas en una lista

    for letter in my_string: #Por cada letra en my_string 
        if letter in vocals: #Si la letra está en vocales
            counter += 1 #Añadir 1 al contador
        
    return counter #Retornar el contador

print(return_vocals(input("Digite una cadena de texto: "))) #Print y llamar a la función con el output del parámetro.
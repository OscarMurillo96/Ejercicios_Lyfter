def print_upper_and_lower_cases(my_string): #Parámetro
    total_upper = 0 #Contador de mayúsculas
    total_lower = 0 #Contador de minúsculas
    for string in my_string: #Por cada string en my_string
        if string.isupper(): #Si el caracter isUpper (Mayúscula)
            total_upper += 1 #Añadir uno al contador
        elif string.islower(): #Pero si el caracter isLower (Minúscula)
            total_lower += 1 #Añadir una al contador

    print(f"El resultado es de {total_upper} mayúsculas, y {total_lower} minúsculas")

print_upper_and_lower_cases(input("Ingrese una oración corta: "))

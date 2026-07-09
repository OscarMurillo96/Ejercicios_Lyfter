def print_string_and_dashes(my_string): #Parámetro
    
    hyphen = my_string.split("-") #El método split() convierte el string a lista
    hyphen.sort() #El método sort ordena los elementos alfabéticamente

    return "-".join(hyphen) #El método join()convierte la lista a string y "-" los separa con guiones en vez de espacios

print(print_string_and_dashes(input("Ingrese una lista de palabras: ")))
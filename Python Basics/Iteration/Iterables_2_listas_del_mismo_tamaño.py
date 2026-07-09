first_list = ["Estoy", "esta", "desde", "y", "Studio"]
second_list = ["escribiendo", "lista", "Python", "Visual", "Code"]

for i in range (len(first_list)):
    print(first_list[i], second_list[i])

#Para este ejercicio, descubrí que, for i in range(len(first_list)): lo que hace es generar las posiciones
#que posteriormente va a usar en second_list (0,1,2,3,4) al ser de la misma cantidad de items no es necesario
#llamar la variable second_list
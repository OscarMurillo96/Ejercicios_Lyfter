def sum_numbers_of_list(my_list): #Parámetro my_list
    total = 0 #Una variable total en 0

    for number in my_list: #Por cada número en my_list entonces:
        total += number #total va ser la suma de todos los números

    return total #Devolvemos total

print(sum_numbers_of_list([4, 6, 2, 29])) #Print a los parámetros de la función sum_numbers_of_list

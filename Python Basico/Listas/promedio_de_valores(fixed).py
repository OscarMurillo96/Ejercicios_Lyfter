my_list = []

counter = 1

while counter <= 5:
    number = int(input("Ingrese un número: "))
    my_list.append(number)
    counter += 1

total = 0

#-> Recorrido de los elementos de la lista:
for i in range(len(my_list)): #-> los elementos son sumados a la variable total
    total += my_list[i]

average = total / len(my_list) #->En la variable average se hace la formula total dividido entre los elementos de la lista.
print(f"El promedio es de: {average}")#-> Acá printeo el resultado 

#-> Nueva lista
new_list = []

#-> Recorrido de los elementos de la lista:
for i in range(len(my_list)):
    if my_list[i] > average: #Si los elementos de mi lista son mayores al almacenado en average, entonces...
        new_list.append(my_list[i]) #Añadir esos elementos a la nueva lista usando append

print(f"Nueva lista: {new_list}")
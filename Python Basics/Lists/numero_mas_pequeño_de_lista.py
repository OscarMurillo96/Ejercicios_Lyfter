my_list = []

counter = 1

while counter <= 5:
    number = int(input("Ingrese 5 números aleatorios: "))
    my_list.append(number)
    counter += 1

#Variable de comparación, 
comparison = my_list[0]
#Se toma el índice primero (0), se compara su valor en el ciclo for a continuación:

#Reccorrido de los items de la lista vía su índice:
for i in range(len(my_list)):
        #Esta fué la lógica inicial que yo había pensado, pero, al investigar un poco más:
        #if number in my_list != max(number):
        #print(f"El número más pequeño es{[i]}")
        #Hacía falta una variable de comparación

#La lógica después de mi investigación fué la siguiente:
    #Si los ítems de mi lista son menores a el primer elemento que es el índice 0 entonces:
    if my_list[i] < comparison:
        #El número en la variable comparison va a reemplazar ese número con el índice que es menor comparado con el que está en la posición (0)
        comparison = my_list[i]
print(f"El número menor en la lista es {comparison}")

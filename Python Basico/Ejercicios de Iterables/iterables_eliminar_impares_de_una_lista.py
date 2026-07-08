my_list = [10, 11, 20, 21, 30, 31, 40, 41]

for i in range(len(my_list)):
    if my_list [i] % 2 == 0:
        print(my_list [i])

#De este ejercicio aprendí a leerlo de esta forma: 
#Primero, recorrer la lista con range() y len()
#Segundo, condición: si los elementos de my_list son divisibles por 2 y el resultado de su cociente es 0, es par.
#Tercero, imprimir los elementos de my_list usando esa condición if.
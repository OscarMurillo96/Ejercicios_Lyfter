list_a = ['first_name', 'last_name', 'role']
list_b = ['Oscar', 'Murillo', 'Senior QA Engineer']

my_dictionary = {} #En esta variable se van a asignar las keys y values de las listas.

for i in range(len(list_a)): #list_a y list_b comparten el mismo índice, recorrido simultáneo
    my_dictionary[list_a[i]] = list_b[i] #my_dictionary va a tener el valor de los índices simultáneamente:

print(my_dictionary) #Es por eso que imprime índice 0 con 0, 1 con 1, y 2 con 2
my_list = []

counter = 1

while counter <= 5:
    word = input("Ingrese una palabra: ")
    my_list.append(word)
    counter += 1

new_list = []

for i in range(len(my_list)): #Recorrido de la lista
    #Según como yo lo entiendo, la lógica con mis palabras es la siguiente:
    if len(my_list[i]) > 4: #Si la longitud del item de la lista (my_list) es mayor a 4
        new_list.append(my_list[i]) #Se añade a la nueva lista.
#Y por último, se imprime esa nueva lista
print(new_list)

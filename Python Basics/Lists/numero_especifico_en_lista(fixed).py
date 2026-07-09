my_list = []
counter = 1

while counter <= 10:
    ten_numbers = int(input("Digite 10 números aleatorios (Se pueden repetir): "))
    my_list.append(ten_numbers)
    counter += 1

search_number = int(input("Digite el número que desea buscar: "))

occurrences = 0

for i in range(len(my_list)):
    if my_list[i] == search_number:
        occurrences += 1
    
if occurrences > 0:
    print(f"El número {search_number} se repite {occurrences} veces")
else:
    print("El número ingresado no se repite ninguna vez")
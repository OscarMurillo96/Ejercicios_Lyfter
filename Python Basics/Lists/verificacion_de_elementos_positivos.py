my_list = []

counter = 1
positives = 0
negatives = 0

while counter <= 5:
    number = int(input("Ingrese 5 números: "))
    my_list.append(number)
    if number > 0:
        positives += 1 
    else:
        negatives += 1
    counter += 1

print(my_list)

if negatives > 0:
    print("Hay almenos un número negativo o cero.")
else:
    print("Todos los números son positivos.")

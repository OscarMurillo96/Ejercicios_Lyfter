ten_numbers = []

counter = 1
while counter <= 10:
    number = int(input("Ingrese 10 números: "))
    ten_numbers.append(number)
    counter += 1

print(ten_numbers)
print("El número más alto fué", max(ten_numbers))

#Para este ejercicio entendí lo siguiente:
#Primero, crear la lista vacía ten_numbers []
#Segundo, pedir el numero con la variable number
#Tercero, a la lista ten_numbers guardarle los 10 valores de number usando .append
#Cuarto, imprimir ten_numbers (lista)
#Quinto, sacar el numero mas alto usando max()
number_one = int(input("Digite el primer número: "))
number_two = int(input("Digite el segundo número: "))
number_three = int(input("Digite el tercer número: "))

if number_one > number_two and number_one > number_three:
    print(f"El número mayor es: {number_one}")
elif number_two > number_one and number_two > number_three:
    print(f"El número mayor es: {number_two}")
else:
    print(f"El numero mayor es: {number_three}")


#Investigando, encontré que este ejercicio puede ser simplificado a menos lineas de código usando max() y evitando usar if y elif:
print(f"El numero mayor es: {max(number_one, number_two, number_three)}")

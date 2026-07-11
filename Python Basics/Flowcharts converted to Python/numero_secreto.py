import random

secret_number = random.randint(1, 10)
user_number = int(input("Ingrese un número del 1 al 10: "))

while user_number != secret_number:
    user_number = int(input("Número incorrecto, intente nuevamente: "))
else:
    print(f"Número correcto, el número secreto es: {secret_number}")

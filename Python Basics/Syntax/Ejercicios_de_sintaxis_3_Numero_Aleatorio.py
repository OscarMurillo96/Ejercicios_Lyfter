import random

secret_number = random.randint(1, 10)
number_guess = int(input("Digite un número aleatorio: "))

while number_guess != secret_number:
    number_guess = int(input("Numero incorrecto, intente nuevamente con otro número: "))
print(f"Numero correcto, en efecto el número es: {secret_number}")
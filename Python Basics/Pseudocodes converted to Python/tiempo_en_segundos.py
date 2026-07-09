seconds = int(input("Por favor ingrese el tiempo en segundos: "))

if seconds < 600:
    remaining = 600 - seconds
    print(f"Le restan {remaining} segundos para llegar a 10 minutos.")
elif seconds == 600:
    print("El tiempo en segundos ingresado es igual a 10 minutos exactos.")
else:
    print("El tiempo ingresado en segundos es mayor a 10 minutos.")
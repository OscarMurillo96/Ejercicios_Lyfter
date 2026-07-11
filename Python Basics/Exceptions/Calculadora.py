def calculate(): #Función calcular
    print("Calculadora de Oscar v1.0.0.0")
    print("********************************************************************************************************************")
    current_number = int(input("Digite un número: ")) #Número actual
    print("********************************************************************************************************************")

    while True: #Loop infinito
        try: #Intentar en caso de ser positivo
            print("Menú de opciones: \n 1. SUMA(+)\n 2. RESTA(-)\n 3. MULTIPLICACIÓN (*)\n 4. DIVISIÓN(/)\n 5. BORRAR DATOS(C)") #Imprimir un menú de opciones.
            print("***********************************************************************************************************")
            print(current_number) #Aquí el número que está en memoria
            print("***********************************************************************************************************")
            user_selection = int(input("Ingrese un valor del 1 al 5: ")) #Pide al usuario ingresar las opciones disponibles.
            if user_selection != 5: #Si la selección del usuario no es 5, sigue esta lógica:
                second_number = int(input("Digite el segundo número: ")) #Pide al usuario un segundo valor.
            if user_selection == 1: #Si el usuario quiere una suma:
                current_number = current_number + second_number
            elif user_selection == 2: #Si el usuario quiere una resta:
                current_number = current_number - second_number
            elif user_selection == 3: #Si el usuario quiere una multiplicación:
                current_number = current_number * second_number
            elif user_selection == 4: #Si el usuario quiere una división:
                current_number = current_number / second_number
            else: #Sino, si el usuario ingresa un número fuera del rango 1 a 5
                print("***********************************************************************************************************")
                print("El número ingresado no pertenece a ninguna opción")
                print("***********************************************************************************************************")
            if user_selection == 5: # Si la selección del usuario es borrar los datos:
                print("***********************************************************************************************************")
                print("Datos borrados")
                current_number = int(input("Digite un número: ")) #Vuelve a solicitar el primer número.
                print("***********************************************************************************************************")
            else:
                print("***********************************************************************************************************")
                print(f"El resultado de la operación es {current_number}") #Sino, devuelve el resultado de las operaciones.
                print("***********************************************************************************************************")
        except ValueError as error: #Si hay un error de valor, si el usuario ingresa un string en vez de un int, vamos a imprimir esta excepción junto al detalle del error.
            print("***********************************************************************************************************")
            print(f"El carácter ingresado en el menú no es un cáracter válido. Detalles del error: {error}")
            print("***********************************************************************************************************")
        except ZeroDivisionError as error: #Si hay un error de división, si el usuario divide un número por 0, vamos a imprimir esta excepción junto al detalle del error.
            print("***********************************************************************************************************")
            print(f"Ningún número es divisible por cero. Detalles del error: {error}")
            print("***********************************************************************************************************")

calculate()
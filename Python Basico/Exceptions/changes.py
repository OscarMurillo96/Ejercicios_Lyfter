def display_options_menu_and_user_selection():
    print("********************************************************************************************************************")
    print("Menú de opciones: \n 1. SUMA(+)\n 2. RESTA(-)\n 3. MULTIPLICACIÓN (*)\n 4. DIVISIÓN(/)\n 5. BORRAR DATOS(C)") #Imprimir un menú de opciones.
    print("********************************************************************************************************************")
    #Try and except para manejar la lógica de errores si un cáracter es inválido.
    try:
        user_selection = int(input("Ingrese un valor del 1 al 5: ")) #Pide al usuario ingresar las opciones disponibles.
        return user_selection #Retornar el input.
    except ValueError as error: #Error handling si hay un cáracter inválido.
        print("********************************************************************************************************************")
        print(f"El cáracter ingresado en el menú no es un cáracter válido. Detalles del error: {error}")
        print("********************************************************************************************************************")
        return None #Si el usuario ingresa otro valor no numeral, None evita que la asignación quede vacía en user_selection


def math_operation(current_number, user_selection): #Parámetros
    try:
        if user_selection == 1: #Si el usuario selecciona 1, va a generar una suma:
            second_number = int(input("Digite un segundo número a sumar: "))
            current_number = current_number + second_number
        elif user_selection == 2: #Si el usuario selecciona 2, va a generar una resta:
            second_number = int(input("Digite un segundo número a restar: "))
            current_number = current_number - second_number
        elif user_selection == 3: #Si el usuario selecciona 3, va a generar una multiplicación:
            second_number = int(input("Digite un segundo número a multiplicar: "))
            current_number = current_number * second_number
        elif user_selection == 4: #Si el usuario selecciona 4, va a generar una división:
            second_number = int(input("Digite un segundo número a dividir: "))
            current_number = current_number / second_number
        elif user_selection == 5: #Si el usuario selecciona 5, va a borrar los datos de current_number y solicitar un número nuevo
            print("********************************************************************************************************************")
            print("Datos borrados.")
            print("********************************************************************************************************************")
            while True: #Ciclo infinito, el cuál se va a repetir hasta que se ingrese un cáracter válido
                try:
                    current_number = int(input("Digite un número: ")) #Número actual
                    break
                except ValueError as error: #Error handling si hay un cáracter inválido.
                    print(f"Error, el cáracter ingresado no es válido, intente nuevamente. Detalles: {error}")
        else: #Si ninguna de las opciones anteriores se cumple, se ejecuta else:
            print("********************************************************************************************************************")
            print("El número ingresado no pertenece a ninguna opción")
            print("********************************************************************************************************************")
        if user_selection in [1, 2, 3, 4]: #Si el user_selection es 1, 2, 3, o 4 imprimir este resultado:
            print("********************************************************************************************************************")
            print(f"El resultado de la operación es {current_number}")
            print("********************************************************************************************************************")
    except ZeroDivisionError as error: #Error handling de división por cero.
        print("********************************************************************************************************************")
        print(f"Ningún número es divisible por cero. Detalles del error: {error}")
        print("********************************************************************************************************************")
    return current_number


def loop_action():
    while True: #Ciclo infinito, el cuál se va a repetir hasta que se ingrese un cáracter válido
        try:
            current_number = int(input("Digite un número: ")) #Número actual
            break
        except ValueError as error:
            print("********************************************************************************************************************")
            print(f"Error, el cáracter ingresado no es válido, intente nuevamente. Detalles: {error}")
            print("********************************************************************************************************************")
    while True: #Ciclo de la lógica de la calculadora
        user_selection = display_options_menu_and_user_selection()
        current_number = math_operation(current_number, user_selection)


def main(): #Función principal llama a otras funciones menos a display_options_menu_and_user_selection() y math_operation porque se retornan a sí mismas
    loop_action()
main()
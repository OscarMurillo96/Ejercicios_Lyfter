def request_string_to_user():
    string = input("Digite una cadena de texto: ") #Pedir un string al usuario.
    return string #Retorna el string


def add_line_to_the_file(path, new_string): #Path y new string como parámetros.
    with open(path, 'a', encoding="utf-8") as file: #Método 'a' de append, puesto que vamos a agregar datos a un archivo.
        file.write(new_string + "\n") #Método de escritura, separado por un salto de línea.


def main():
    user_string = request_string_to_user() #Llamar a la función request_string_to_user y guardarla en una variable.
    add_line_to_the_file("Manejo de Archivos/existing_text_file.txt", user_string) #Darle la ruta a la función add_line_to_the_file, y el string que el usuario escribió
main()
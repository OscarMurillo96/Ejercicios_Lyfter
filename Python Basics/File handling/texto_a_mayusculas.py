def read_file(path): #Path como parámetro
    with open(path, 'r', encoding="utf-8") as file: #Con el archivo definido en path abierto como file:
        return file.readlines() #Retornar el contenido línea por línea


def convert_to_upper(content): #Content como parámetro
    my_list = [] #Lista vacía
    for word in content: #Por cada palabra del contenido
        my_list.append(word.upper()) #Añadirla a la lista vacía en Uppercase.
    return my_list #Retornar la lista.


def output_file(new_path, new_string): #Nuevo path, y nuevo string como parámetros.
    with open(new_path, 'w', encoding="utf-8") as output_file: ##Con el nuevo path como archivo de salida:
        output_file.writelines(new_string) #Nuevo archivo de salida, escribir nuevo string en nuevas líneas.


def main():
    read = read_file("Manejo de Archivos/lower_case_text.txt") #Read va a abrir la función read_file que contiene la ruta original del archivo.
    convert = convert_to_upper(read) #Convert llama a la función convert_to_upper, que convierte el texto a Mayúscula y lo guarda en una lista.
    output_file("Manejo de Archivos/upper_case_text.txt", convert) #Llama a la función que crea el nuevo archivo, y a la vez recibe el contenido convertido anteriormente en content.
main()
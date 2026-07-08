def read_file(path): #Path como parámetro.
    with open(path, 'r', encoding="utf-8") as file: #Con el archivo definido en path abierto como file:
        return file.read() #Retornar la lectura del archivo.


def word_counter(content): #Content como parámetro.
    words = content.split() #Dividir las palabras en espacios y saltos de línea.
    return len(words) #Retornar el conteo de las palabras.


def main():
    read = read_file("Manejo de Archivos/text.txt") #Read para guardar el resultado de la lectura del archivo.
    counter = word_counter(read) #Counter llama a la función que hace conteo y split
    print(f"El texto contiene {counter} palabras") #Texto final
main()


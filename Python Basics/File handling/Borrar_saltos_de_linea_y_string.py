def read_file(path): #Path como parámetro
    with open(path, 'r', encoding='utf-8') as file: #Leer el archivo 'r'
        return file.read() #Retornar la lectura del archivo


def processing_text(string): #String como parámetro
    lines = string.split("\n") #Split divide el string y remueve el salto de línea
    result = " ".join(lines) #Join une el string, y los espacia " "
    return result


def write_the_result(new_path, new_string): #Nuevo path y nuevo string
    with open(new_path, "w", encoding="utf-8") as output_file: #Con la apertura de new_path 'w' utf-8 como archivo de salida:
        output_file.write(new_string) #Escribir nuevo string en archivo de salida.


def main():
    content = read_file("Manejo de Archivos/file.txt") #Content es igual a darle el path a la función de read_file
    result = processing_text(content) #Result va a ser igual a aplicarle la función processing_text que es quién divide y espacia el string que le pasamos a content
    write_the_result("file2.txt", result) #la función write the result recibe el nombre del nuevo archivo y el resultado de la conversión.
main()

def request_name(): #Parámetro nombre
        name = input("Digite su nombre: ")
        if name.isdigit(): #Si el nombre es un dígito (número)
            raise ValueError("El campo de nombre no puede contener valores numéricos.") #Raise, ejecutado en main.
        
        return name #Si es correcto, retorna el valor de name.


def request_age(): #Parámetro edad
    age = input("Digite su edad: ")
    return age #Retorna age si es correcto.


def main():
    try: #Intenta el valor de name, y si no es correcto:
        name = request_name()
    except ValueError as error: #Captura el raise de request_name
        print(error)
        return None #No retorna ningún valor
    
    try:
        age = request_age() #Llama a la función
        age = int(age) #Convierte el dato de string a integer
        print(f"Hola {name}, su edad es {age} años")
    except ValueError as error:
        print(f"Error, edad inválida. Detalles: {error}")
        return None #No retorna ningún valor
main()
#1. Intente acceder a una variable definida dentro de una función desde afuera.
def print_hello_world():
    x = "Hello World" #La variable x por si sola no retorna ningún valor
    return x #Se debe agregar return para que no haya error

result = print_hello_world() #Creamos una variable con el valor de esa función
print(result) #E imprimomos esa variable.


#2. Intente acceder a una variable global desde una función y cambiar su valor.
x = "Goodbye Universe" #Variable global

def change_global():
    global x #Con esta indicación referimos la variable global llamada x
    x = "Hello World" #Y cambiamos el valor de la variable

change_global() #Llamamos a la función
print(x) #E Imprimimos el nuevo valor de la variable.


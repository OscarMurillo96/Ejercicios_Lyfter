"""Cree una función que imprima “Hola, [nombre]” dos veces:
Cree un decorador @repeat_twice que haga que la función decorada se ejecute dos veces seguidas, con los mismos argumentos"""

def repeat_twice(func):
    def wrapper(*args, **kwargs): #Wrapper
        func(*args, **kwargs) #Executes the original function
        func(*args, **kwargs) #Executes the original function
    return wrapper

@repeat_twice #Decorator
def greet(name):
    print(f"Hello, {name}")


greet("Oscar")
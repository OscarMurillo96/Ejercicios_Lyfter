"""Cree una función que se llame multiply, la cual obtiene dos valores y los multiplica entre si
A esta función se le debe combinar dos decoradores:
@log_call: imprime el nombre de la función, los argumentos, fecha actual y el retorno
@validate_numbers: revisa que todos los argumentos sean numéricos"""
import datetime as dt

def validate_numbers(func):
    def wrapper(*args, **kwargs): #Wrapper
        #Args validation
        for element in args: 
            if isinstance(element, bool): #Check if the argument is a boolean type
                raise TypeError("Arguments can't be boolean type.")
            if not isinstance(element, (int, float)): #Check if the argument is not int or float
                raise TypeError(f"Argument of type {type(element).__name__} is not allowed. Expected int or float.")

        #Kwargs validation
        for value in kwargs.values(): #Direct function
            if isinstance(value, bool): #Check if the argument is a boolean type
                raise TypeError("Arguments in kwargs can't be boolean type.")
            if not isinstance(value, (int, float)): #Check if the value is not int or float
                raise TypeError(f"Argument of type {type(value).__name__} is not allowed. Expected int or float.")
        # If validation passes, call the original function and save the result    
        x = func(*args, **kwargs)
        return x
    return wrapper


def log_call(func):
    def wrapper(*args, **kwargs):
        now = dt.datetime.now() #Get the current date and time
        result = func(*args, *kwargs) #Execute the original function and store the result
        print(f"Function name: {func.__name__} - Args: {', '.join(map(str, args))} - [{now}] - Result: {result}") #Print the function call details: name, arguments, timestamp, and result
        return result
    return wrapper

@log_call
@validate_numbers
def multiply(a, b):
    return a * b

print(multiply(3, 4))
print(multiply("text", 4))
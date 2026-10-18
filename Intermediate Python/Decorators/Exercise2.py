"""Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así."""

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

@validate_numbers #Decorator
def addition(num1, num2): 
    result = num1 + num2
    return result


print(addition(3, 4))
print(addition(num1= 3, num2 = 4))
print(addition("Hello World", 4))
print(addition(num1 = "Hello World", num2 = 4))

"""Cree un decorador que haga print de los parámetros y retorno de la función que decore."""

def print_parameters(func): #Decorator: receives the original function
    def wrapper(*args, **kwargs): #Catch any argument
        print(args, kwargs) #Prints the received parameters
        y = func(*args, **kwargs) #Calls the original function and saves its output
        print(y) #Shows the saved output
        return y #Delivers the output to whom called it
    return wrapper #Returns the wrapper

@print_parameters
def addition(num1, num2):
    result = num1 + num2
    return result #Returns the sum

@print_parameters 
def three_parameters(greeting, num3, num4):
    my_result = num3 + num4
    return greeting, my_result #Returns the greeting and the sum

@print_parameters 
def no_parameters():
    return "Hello from Python"

#Two parameters
print(addition(3, 4)) 
print(addition(num1 = 3, num2 = 4)) 

#Three parameters
print(three_parameters("hello", 4, 5))
print(three_parameters("Hello, again", num3=4, num4=5)) 

#No parameters
print(no_parameters())
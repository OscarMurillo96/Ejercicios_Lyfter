"""Cree un decorador @requires_login que:
Verifique si la variable global user_logged_in es True
Si no lo es, debe lanzar una excepción "Usuario no autenticado"
Si lo es, la función decorada se ejecuta normalmente"""


def requires_login(func):
    def wrapper(*args, **kwargs): #Wrapper
        global user_logged_in #Accessing the global variable
        if not user_logged_in: #If the user is not logged in
            raise Exception("User must be logged to see user's profile.") #Exception
        x = func(*args, *kwargs) #If the logic gets here, save the function into a variable and then...
        return x #Return the variable a.k.a complete decorated function
    return wrapper

@requires_login
def view_profile():
    print("Showing the user's profile")


user_logged_in = True
view_profile()
user_logged_in = False
view_profile()
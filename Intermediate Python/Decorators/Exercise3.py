"""Cree una clase de User que:
Tenga un atributo de date_of_birth.
Tenga un property de age.
Luego cree un decorador para funciones que acepten un User como parámetro que se encargue de revisar si el User es mayor de edad y arroje una excepción de no ser así."""

import datetime as dt

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property #Property
    def age(self):
        today = dt.date.today() #Gets today's date
        age = today.year - self.date_of_birth.year #Calculates the difference of years
        #Creates a date using the current year but with the month and day of birth
        #This helps you figure out if this year's birthday has already passed
        is_birthday = dt.date(today.year, self.date_of_birth.month, self.date_of_birth.day) 
        if today < is_birthday:  #If today is before this year's birthday
            age -= 1 #It hasn't been that person's birthday yet, so there's 1 left
        return age

    def __str__(self):
        return f"User (age: {self.age})" #Prints the user's current age


def is_legal_age(func):
    def wrapper(*args, **kwargs): #Wrapper
        user = args[0] #Get the User from the first argument
        if user.age < 18: #If the user's age is less than 18
            raise ValueError("User must be 18 or older.")
        result = func(*args, **kwargs) #Executes the original function
        return result #And returns the result
    return wrapper

@is_legal_age #Decorator
def buy_some_beer(user):
    return f"{user} can buy beer 🍻🍻🍻"


user1 = User(dt.date(1996, 10, 17))
user2 = User(dt.date(1995, 1, 18))
user3 = User(dt.date(1994, 5, 16))
child_user = User(dt.date(2015, 11, 14))

#A child user is attempting to buy beer
print(buy_some_beer(child_user)) #Comment this line to see below's output

#An adult user is attempting to buy beer
print(buy_some_beer(user1))
print(buy_some_beer(user2))
print(buy_some_beer(user3))
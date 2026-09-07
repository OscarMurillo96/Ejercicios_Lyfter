class Animal:
    def __init__(self, name):
        self.name = name #Name


    def speak(self):
        return ("Makes a sound!") #Animal debe tener nombre y método speak() que retorne "Hace un sonido"


class Dog(Animal):
    def speak(self):
        return ("Guau") #Dog debe sobrescribir speak() para decir "Guau"


class Cat(Animal):
    def speak(self):
        return ("Miau") #Cat debe sobrescribir speak() para decir "Miau"

#Output
dog = Dog("Firulais")
print(dog.speak())

cat = Cat("Michi")
print(cat.speak())

animal = Animal("Animal")
print(animal.speak())
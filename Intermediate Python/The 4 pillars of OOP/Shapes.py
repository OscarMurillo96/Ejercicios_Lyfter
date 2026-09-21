from abc import ABC, abstractmethod #Importing the abstract method
from math import pi #Importing math to use pi

class Shape(ABC): #Inherits from ABC
    @abstractmethod
    def calculate_area(self): #Must be implemented by subclasses
        pass


    @abstractmethod
    def calculate_perimeter(self): #Must be implemented by subclasses
        pass


class Circle(Shape): #Inherits from Shape
    def __init__(self, radius):
        self.radius = radius


    def calculate_area(self): #Calculates the circle area
        return pi * (self.radius ** 2)


    def calculate_perimeter(self): #Calculates the circle perimeter
        return 2 * pi * (self.radius)


class Square(Shape): #Inherits from Shape
    def __init__(self, side):
        self.side = side


    def calculate_area(self): #Calculates the square area
        return self.side ** 2


    def calculate_perimeter(self): #Calculates the square perimeter
        return self.side * 4


class Rectangle(Shape): #Inherits from Shape
    def __init__(self, height, width): 
        self.height = height
        self.width = width


    def calculate_area(self): #Calculates the rectangle area
        return self.height * self.width


    def calculate_perimeter(self): #Calculates the rectangle perimeter
        return 2 * self.width + 2 * self.height


circle = Circle(5)
print(round(circle.calculate_area(), 2))
print(round(circle.calculate_perimeter(), 2))

square = Square(4)
print(square.calculate_area())
print(square.calculate_perimeter())

rectangle = Rectangle(3, 6)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

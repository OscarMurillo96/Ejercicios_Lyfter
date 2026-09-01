import math #this module includes the pi value

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

circle = Circle(2)
print(round(circle.get_area(), 2))

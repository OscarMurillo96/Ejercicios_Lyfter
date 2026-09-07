class Rectangle:
    def __init__(self, width, height): # init method, receives: self, width and height
        if width < 0 or height < 0: #Condition, if width is less to 0 (negative) or height is less to 0 (negative)
            raise ValueError("There's a negative value, values must be positives!") #Raise a ValueError with a custom message
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height #To get the Rectangle area, multiply width by height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height #To get the perimeter, multiply 2 by width plus 2 by height

width_input = int(input("Input the width: ")) #User input
height_input = int(input("Input the height: ")) #User input

try: #Error handling
    rectangle = Rectangle(width_input, height_input) # The Rectangle class will have the values inputted in the above variables
    print(rectangle.get_area()) #Calls the get_area() function
    print(rectangle.get_perimeter()) #Calls the get_perimeter() function
except ValueError as error: #Error handling
    print(f"There was an error, details: {error}") #Prints the error message caught from the exception
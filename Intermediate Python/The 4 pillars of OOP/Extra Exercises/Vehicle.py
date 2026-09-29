class Vehicle: #Parent class
    def __init__(self, brand, year):
        self._brand = brand #Protected attribute
        self._year = year #Protected attribute


    def get_info(self):
        return f"Brand: {self._brand}\nYear: {self._year}\n"


class Car(Vehicle): #Inherits from Vehicle
    def __init__(self, brand, year, doors):
        super().__init__(brand, year) #Calls the parent method and initializes the attributes
        self.doors = doors


    def get_info(self):
        return super().get_info() + f"Doors: {self.doors}"


class Motorcycle(Vehicle):
    def __init__(self, brand, year, m_type):
        super().__init__(brand, year) #Calls the parent method and initializes the attributes
        self.m_type = m_type


    def get_info(self):
        return super().get_info() + f"Type: {self.m_type}"


car = Car("Toyota", 2021, 4)
print(car.get_info())
print("-----------------------------------------")
motorcycle = Motorcycle("Kawasaki", 2020, "Sport")
print(motorcycle.get_info())
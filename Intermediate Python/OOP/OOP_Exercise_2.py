class Bus:
    def __init__(self, max_passengers):
        self.current_passengers = [] #A list to store the number of the current passengers
        self.max_passengers = max_passengers #Maximum capacity of the bus


    def add_passengers(self, person):
        if len(self.current_passengers) < self.max_passengers: #If the length of current passengers is less than the maximum of passengers
            self.current_passengers.append(person) #Add a person to the current passengers list.
        else:
            print("Bus is full") #Else, print an error message.


    def remove_passengers(self, person):
        if person in self.current_passengers: #If the person is currently in current_passengers:
            self.current_passengers.remove(person) #Remove the person from the list
            print("the passenger left the bus") #Prints a message letting know the person has left the bus
        else:
            print("Passenger not found.") #If the person does not exist, print an error message


class Person:
    def __init__(self, passenger_name):
        self.passenger_name = passenger_name #Store the passenger's name


bus = Bus(52) #Creates a bus with a capacity of 52 passengers
person_one = Person("Oscar") #Creates a Person instance named Oscar
person_two = Person("Pythonicio") #Creates a Person instance named Pythonicio

bus.add_passengers(person_one) #Adds person one "Oscar" to the bus
bus.add_passengers(person_two) #Adds person two "Pythonicio" to the bus

bus.remove_passengers(person_one) #Removes person one "Oscar" from the bus
bus.remove_passengers(person_one) #Attempts to remove "Oscar" from the bus, but instead, throws an error message ("Passenger not found.")
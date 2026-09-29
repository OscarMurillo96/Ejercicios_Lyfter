class Employee: #Class Employee
    def __init__(self, _name, _salary):
        self._name = _name #protected
        self.salary = _salary #protected


    @property #property
    def name(self):
        return self._name


    @property #property
    def salary(self):
        return self._salary


    @salary.setter #setter attribute
    def salary(self, value):
        if value < 0:
            raise ValueError(f"The salary can't be {value}.")
        elif (value >= 0):
            self._salary = value


    def promote(self, percentage):
        self.salary += self.salary * percentage


employee = Employee("Oscar", 150000)
employee.promote(0.1) #promotion percentage
print(employee.salary)

from abc import ABC, abstractmethod #Importing the abstract method

class User(ABC): #Abstract class


    @abstractmethod #decorator
    def get_role(self):
        pass


    @abstractmethod #decorator
    def has_permission(self, permission):
        pass


class AdminUser(User): #Inherits from User
    def __init__(self, name):
        self.name = name #User name


    def get_role(self):
        return "Admin User."


    def has_permission(self, permission):
        return True


class RegularUser(User): #Inherits from User
    def __init__(self, name):
        self.name = name


    def get_role(self):
        return "Regular user."


    def has_permission(self, permission):
        if permission == "read":
            return True
        else:
            return False


admin = AdminUser("Oscar")
print(admin.get_role())
print(admin.has_permission("write"))
print(admin.has_permission("delete"))
print("-----------------------------")
regular = RegularUser("User")
print(regular.get_role())
print(regular.has_permission("read"))
print(regular.has_permission("write"))
print(regular.has_permission("delete"))
print("-----------------------------")
print(f"Admin Name:  {admin.name}")
print(f"Regular User Name: {regular.name}")
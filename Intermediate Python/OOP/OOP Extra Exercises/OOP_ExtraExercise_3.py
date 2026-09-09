class Product:
    def __init__(self, name, price, quantity): #Nombre, precio y cantidad
        self.name = name
        self.price = price
        self.quantity = quantity

"""Cree una clase Inventory que:
- Guarde productos en una lista
- Tenga métodos para:
- Agregar un producto
- Mostrar todos los productos
- Calcular el valor total del inventario"""
class Inventory:
    def __init__(self):
        self.products = [] #Empty list


    def add_products(self, product): #Agregar un producto
        self.products.append(product) #Add product to products list


    def show_all(self): #Mostrar todos los productos
        for product in self.products: #For each product in the list: 
            print(f"Product Name: {product.name}, \n Product Price: {product.price}, \n Product Quantity: {product.quantity}")


    def calculate_total(self): #Calcular el valor total del inventario
        total = 0 #Variable initialized in 0
        for product in self.products: #For each product in the list: 
            total = total + (product.price * product.quantity) #The total is the multiplication of the price by the quantity
        return total


product_one = Product("Mouse", 5000, 3) #Product one, value: 5000, quantity: 3
product_two = Product("Keyboard", 8000, 2) #Product two, value: 8000, quantity, 2

inventory = Inventory()
inventory.add_products(product_one) #Adding product one to the list
inventory.add_products(product_two) #Adding product two to the list

inventory.show_all() #Show all products
print(inventory.calculate_total()) #Total
products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

result = {}
for product in products: #Por cada producto en products
    cat = product['category'] #cat busca directamente la key 'category' de cada producto en products.
    price = product['price'] #price busca directamente la key 'price' de cada producto en products.

    if cat in result: #Si la cat ya se encuentra en result:
        result[cat] += price #A esa cat le sumamos el price (no se usa append por ser un valor integer)
    else:
        result[cat] = price #Sino, se crea una nueva cat y un price

print(result) #Imprimo el resultado


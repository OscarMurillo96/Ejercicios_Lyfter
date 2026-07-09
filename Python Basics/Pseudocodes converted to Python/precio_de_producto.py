product_price = int(input("Ingrese el precio del producto: "))
discount = 0

if product_price < 100:
    discount = product_price * 0.02
elif product_price >= 100:
    discount = product_price * 0.10

final_price = product_price - discount
print(f"El precio final del producto es de: {final_price}")

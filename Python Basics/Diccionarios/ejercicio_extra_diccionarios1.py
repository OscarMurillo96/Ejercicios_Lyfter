sale_list = [
    {
        'date' : '5/21/2026',
        'customer_email' : 'oscarsantosmurillo@outlook.com',
        'items' : [
            {'name' : 'Lava Lamp', 'upc' : 'ITEM-1234', 'unit_price' : 12500},
            {'name' : 'Iron','upc' : 'ITEM-1221','unit_price' : 10000},
            {'name' : 'Basketball','upc' : 'ITEM-2103','unit_price' : 17750},
        ],
    },

    {
        'date' : '5/20/2026',
        'customer_email' : 'zsan.mur@gmail.com',
        'items': [
            {'name' : 'Lava Lamp','upc' : 'ITEM-1234','unit_price' : 12500}, 
            {'name' : 'Key Holder','upc' : 'ITEM-2001','unit_price' : 2500}, 
        ],
    },

    {
        'date' : '5/19/2026',
        'customer_email' : 'oscarsantosmurillo3@gmail.com',
        'items': [
            {'name' : 'Key Holder','upc' : 'ITEM-2001','unit_price' : 2500},
            {'name' : 'Basketball','upc' : 'ITEM-2103','unit_price' : 17750},
        ],
    },

]

result = {}

for sale in sale_list: #Por cada sale en sale_list:
    for item in sale['items']: #Por cada ítem en sale (Acá apunta a el key items)
        upc = item['upc'] #La variable upc va a tomar el valor de 'upc' en 'items'
        price = item['unit_price']#La variable price va a tomar el valor de 'unit_price' en 'items'
        if upc in result: #Si el upc ya está dentro del diccionario vacío result:
            result[upc] += price #Al key 'upc' le sumamos el valor de 'price'
        else:
            result[upc] = price #Sino, solo se almacena el 'upc' y el 'price'

print(result) #Imprimimos el resultado
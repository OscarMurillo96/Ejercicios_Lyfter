my_list = [10, 12, 1, 9, 4, 7, 0, 21, 55]

my_list[0], my_list[-1] = my_list[-1], my_list[0]

for i in range(len(my_list)):
    print(my_list[i])

#Según lo que entendí de este ejercicio, es que: 
#En python, el 0 apunta al índice del inicio [0], y [-1] siempre apunta al item final, en este caso 55
#segun la sintáxis 10 es igual a (a) y 55 es igual a (b), con esa formula, se intercambian en una variable: a, b = b, a
#Por ultimo, se recorre la lista con range() y len() y se printea la lista y el indice my_list[i]

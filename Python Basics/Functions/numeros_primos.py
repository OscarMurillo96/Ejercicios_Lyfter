def is_prime(number): #Parámetro
    if number <= 1: #Si number es menor o igual a 1
        return False #Retorna False
    for i in range(2, number): #Por cada posición en el rango de 2 hasta number
        if number % i == 0: #Si el residuo de dividir number entre i es igual a 0
            return False #Retorna False
    return True #Retorna True

def filter_prime_numbers(my_list): #Parámetro
    numbers = [] #Lista vacía
    for number in (my_list): #Por cada number en my_list
        if is_prime(number): #Si el número (llama a la función is_prime) entonces:
            numbers.append(number) #A la lista vacía se le agregan esos números

    return numbers #Retornar la lista con los números

print(filter_prime_numbers([1, 4, 6, 7, 13, 9, 67])) #Los valores del parámetro
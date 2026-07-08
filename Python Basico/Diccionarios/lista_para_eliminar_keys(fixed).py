list_of_keys = ['access_level', 'age']
employee =  {
    'name' : 'Oscar Murillo',
    'email' : 'oscarsantosmurillo@outlook.com',
    'access_level' : 5,
    'age' : 29
}

for i in range(len(list_of_keys)): #Recorrer la lista
    del employee[list_of_keys[i]] #de employee, eliminar los índices de list_of_keys (en este caso access_level y age)

print(employee) #Imprimir lo que queda de employee: todos los datos menos access_level y age.

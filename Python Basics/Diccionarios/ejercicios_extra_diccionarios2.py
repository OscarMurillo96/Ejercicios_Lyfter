employees = [
    {'name':'Oscar','email':'oscarsantosmurillo@outlook.com','department':'IT and Development',},
    {'name':'Zulli','email':'zsan.mur@gmail.com','department':'Logistic',},
    {'name':'Ronald','email':'ronces10@gmail.com.','department':'Customer Service',},
    {'name':'Marlon','email':'marlon-santos@gmail.com','department':'Security',},
    {'name':'Yennian','email':'yennian-santos@gmail.com','department':'Sales',}
]

result = {}

for employee in employees: #Por cada empleado en employees
    dept = employee['department'] #La variable dept almacena el 'department' de ese empleado.

    if dept in result: #Si, el departamento de esa persona ya existe en la variable result:
        result[dept].append(employee['name']) #A ese departamento se le añade el nombre de esa persona vía 'name'
    else:
        result[dept] = [employee['name']] #Sino, se crea un nuevo departamento con el nombre de esa persona.

print(result) #Por último, se imprime ese resultado

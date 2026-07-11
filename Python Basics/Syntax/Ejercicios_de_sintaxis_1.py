#Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
#Si le salen errores, no se asuste. Lealos e intente comprender qué significan.
#Los errores son oportunidades de aprendizaje.
#Por ejemplo:

first_name = input("Digite su nombre: ")
last_name =  input("Digite su primer apellido: ")
second_last_name =  input("Digite su segundo apellido: ")
age = int(input("Digite su edad: "))
salary = float(input("Digite su ingreso mensual en dólares: "))
worker = [
        "Seguro médico", 
        "Seguro privado",
        "Cafetería", 
        "Area de juegos"]

print(f"Hola, Bienvenido/a: {first_name} {last_name} {second_last_name}, su edad es de {age} años, su salario mensual es de {salary}, lo que sería al año {salary * 12}")
print(f"Y sus beneficios como empleado son {', '.join(worker)}")
#Investigando un poco, encontré que la manera más limpia de imprimir los datos de la lista sin comillas ni curly braces es escribir .join

#string + string → ?
name = "Oscar"
lst_name = "Murillo"
print(name + " " + lst_name)

#string + int → ?
print("employee ID:",500200301)

#int + string → ?
print(116500646, "Es la cédula del cliente.")

#list + list → ?
car_list = ["Subaru", "Toyota", "Nissan", "Mazda"]
motorcycle_list = ["Yamaha", "Suzuki", "Honda", "Kawasaki"]

vehicles = car_list + motorcycle_list
print(f"{', '.join(vehicles)}")

#string + list → ?
market = "To Do list: "
super_market_list = ["Comprar manzanas", "comprar uvas", "comprar pan", "comprar jugo de naranja", "comprar jalea"]

to_do_list = market + super_market_list
print("\n".join(to_do_list)) #Error TypeError: can only concatenate str (not "list") to str

#Solución
market = "To Do list: "
super_market_list = ["Comprar manzanas", "comprar uvas", "comprar pan", "comprar jugo de naranja", "comprar jalea"]

print(market)
print("\n".join(super_market_list))

#float + int → ?
monthly_salary = 650_000
months = 12

annual_salary = monthly_salary * months
print(annual_salary)
#Investigando, descubrí que para hacer que 650.000 sea ese valor, el separador debe ser un (_) y no un punto (.)

#bool + bool → ?
is_logged = True
is_online = False


if is_logged == True and is_online == True:
        print("El usuario está Conectado")
elif is_logged == True and is_online == False:
        print("El usuario está offline, pero se encuentra logueado")
else:
        print("El usuario se encuentra offline y deslogueado")





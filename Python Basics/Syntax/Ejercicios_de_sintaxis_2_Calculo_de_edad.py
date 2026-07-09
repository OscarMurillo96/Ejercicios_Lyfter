name = input("Digite su nombre (sin su apellido): ")
last_name = input("Digite su apellido: ")
age = int(input("Digite su edad: "))

if age <= 3:
    print(f"Hola {name} {last_name}, basado en su edad, usted es un bebé")
elif age <= 8 :
    print(f"Hola {name} {last_name}, basado en su edad, usted es un niño")
elif age <= 12 :
    print(f"Hola {name} {last_name}, basado en su edad, usted es un preadolescente")
elif age <= 17 :
    print(f"Hola {name} {last_name}, basado en su edad, usted es un Adolescente")
elif age <= 25 :
    print(f"Hola {name} {last_name}, basado en su edad, usted es un Adulto joven")
elif age <= 50 :
    print(f"Hola {name} {last_name}, basado en su edad, usted es un Adulto")
else:
    print(f"Hola {name} {last_name}, basado en su edad, usted es un Adulto mayor")
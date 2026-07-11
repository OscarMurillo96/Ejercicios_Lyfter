counter = 1
total_approved_grades = 0
total_unapproved_grades = 0
approved_grades_overall = 0
unapproved_grades_overall = 0
total_promedy = 0
grades_total = int(input("Digite el numero de notas a ingresar: "))

while counter <= grades_total:
    current_grade = int(input("Ingrese la nota: "))
    if current_grade < 70:
        total_unapproved_grades = total_unapproved_grades + 1
        unapproved_grades_overall = unapproved_grades_overall + current_grade
    else:
        total_approved_grades = total_approved_grades + 1
        approved_grades_overall = approved_grades_overall + current_grade
    
    total_promedy = total_promedy + current_grade / grades_total
    counter = counter + 1


unapproved_grades_overall = unapproved_grades_overall / total_unapproved_grades
approved_grades_overall = approved_grades_overall / total_approved_grades

print(f"El estudiante tiene esta cantidad de notas aprobadas:{total_approved_grades}")
print(f"Este es el promedio de las notas aprobadas:{approved_grades_overall}")
print(f"El estudiante tiene esta cantidad de notas desaprobadas:{total_unapproved_grades}")
print(f"Este es el promedio de las notas desaprobadas:{unapproved_grades_overall}")
print(f"Promedio total de notas:{total_promedy}")


#Investigando un poco, descubrí que en Python las divisiones por cero generan un error, entonces si el estudiante tiene 0 notas desaprobadas o 0 notas aprobadas el error se va a generar.
#Solución: if total_unapproved_grades > 0:
#    unapproved_grades_overall = unapproved_grades_overall / total_unapproved_grades
#else:
#    unapproved_grades_overall = 0

#if total_approved_grades > 0:
#    approved_grades_overall = approved_grades_overall / total_approved_grades
#else:
#    approved_grades_overall = 0
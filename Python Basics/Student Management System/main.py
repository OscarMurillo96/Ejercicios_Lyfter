from menu import *
from actions import *
from data import *


if __name__ == "__main__":
    students = []
    greeting()
    while True:
        selection = show_menu()
        if selection == 1:
            register_student(students)
        elif selection == 2:
            see_all_students(students)
        elif selection == 3:
            top_three_students(students)
        elif selection == 4:
            see_general_average(students)
        elif selection == 5:
            export_to_csv("students.csv", students)
        elif selection == 6:
            import_from_csv("students.csv", students)
        elif selection == 7:
            see_unapproved_students(students)
        elif selection == 8:
            delete_a_student(students)
        elif selection == 9:
            break
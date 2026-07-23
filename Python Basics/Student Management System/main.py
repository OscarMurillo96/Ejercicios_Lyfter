from menu import *
from actions import *
from data import *


if __name__ == "__main__":
    greeting()
    while True:
        selection = show_menu()
        if selection == 1:
            register_student()
        elif selection == 2:
            see_all_students()
        elif selection == 3:
            top_three_students()
        elif selection == 4:
            see_general_average()
        elif selection == 5:
            export_to_csv("students.csv")
        elif selection == 6:
            import_from_csv("students.csv")
        elif selection == 7:
            see_unapproved_students()
        elif selection == 8:
            delete_a_student()
        elif selection == 9:
            break
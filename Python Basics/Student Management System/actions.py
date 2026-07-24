import re


def error_handling(custom_message, conversion):#Error handling
    while True:
        try:
            user_result = conversion(input(custom_message))
            if user_result >= 0 and user_result <= 100:
                return user_result
            else:
                print("Invalid value, please enter a valid value between 0 and 100")
        except ValueError as error:
            print(f"{custom_message} details: {error}")


def calculate_average(student):#Calculate average function
    average = (student['spanish_grade'] + student['english_grade'] + student['socials_grade'] + student['science_grade']) / 4
    return round(average, 2)


def register_student(students):#Option #1: Register a new student.
    new_student = {}
    while True:
        student_name = input("Enter the student's name: ")
        if not is_valid_name(student_name):
            print("Not a valid name, please try again.")
        else:
            break
    while True:
        section = input("Enter the student's section: ")
        if not is_valid_section(section):
            print("Section must follow the following format (number number letter eg: 01A)")
        else:
            break
    if student_exists(student_name, section, students):
        print("Student is already registered.")
        return
    spanish_grade = error_handling("Enter the Spanish grade: ", float)
    english_grade = error_handling("Enter the English grade: ", float)
    socials_grade = error_handling("Enter the Socials grade: ", float)
    science_grade = error_handling("Enter the Science grade: ", float)
    #Adding the information to the dictionary
    new_student["name"] = student_name
    new_student["section"] = section
    new_student["spanish_grade"] = spanish_grade
    new_student["english_grade"] = english_grade
    new_student["socials_grade"] = socials_grade
    new_student["science_grade"] = science_grade
    students.append(new_student)


def see_all_students(students):#Option #2 See all students.
    if not students:
        print("No students registered yet.")
    else:
        for student in students:
            print(f"{student['name']}\n {student['section']} - Average: {calculate_average(student)}")


def top_three_students(students):#Option #3 Top 3 students.
    if not students:
        print("No students registered yet.")
    
    else:
        sorted_students = sorted(students, key = lambda student: calculate_average(student), reverse = True )
        top_3 = sorted_students[:3]
        for student in top_3:
            print(f"Name: {student['name']}\n Section: {student['section']}\n Average: {calculate_average(student)}")


def see_general_average(students):#Option #4 See general average.
    if not students:
        print("No students registered yet.")
    else:
        general_average = round(sum(calculate_average(student) for student in students) / len(students), 2)
        print(f"General average: {general_average}")


def see_unapproved_students(students):#Option #7 See unapproved students.
    if not students:
        print("No students registered yet.")
    else:
        for student in students:
            grades =  {
                'Spanish' : student['spanish_grade'],
                'English' : student['english_grade'],
                'Socials' : student['socials_grade'],
                'Science' : student['science_grade']
                }
            failed = {subject: grade for subject, grade in grades.items() if grade < 60}
            if failed:
                print(f"Name: {student['name']}, Section: {student['section']}")
                for subject, grade in failed.items():
                    print(f"Subject: {subject}, Grade: {grade}")


def delete_a_student(students): #Option #8 Delete a student.
    if not students:
        print("No students registered yet.")
    else:
        info_name = input("Please enter the student's name: ")
        info_section = input("Please enter the student's section: ")
        found = None
        for student in students:
            if info_name == student['name'] and info_section == student['section']:
                found = student
                break
        if found == None:
                print("Student not found.")
        else:
            confirmation = input(f"Are you sure to delete {student['name']}? (Y/N)")
            if confirmation == "Y":
                students.remove(found)
                print(f"Student {found['name']} has been deleted successfully.")
            else:
                print("Operation cancelled.")


def is_valid_name(name):
    if not name:
        return False
    elif any(character.isdigit() for character in name):
        return False
    return True


def is_valid_section(section):
    if not section:
        return False
    elif not re.match(r'^\d+[A-Z]$', section):
        return False
    return True


def student_exists(name, section, students):
    for student in students:
        if student['name'] == name and student['section'] == section:
            return True
    return False
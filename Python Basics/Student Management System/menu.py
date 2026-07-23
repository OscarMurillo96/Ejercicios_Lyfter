def greeting():
    print("\n Welcome to the student management system - By Oscar Santos Murillo \n")


def show_menu():
    while True:
        try:
            print("Options menu, please select: \n")
            print("1. Register a new student \n")
            print("2. See all students \n")
            print("3. Top 3 students \n")
            print("4. See general average \n")
            print("5. Export to CSV \n")
            print("6. Import from CSV \n")
            print("7. See unapproved students \n")
            print("8. Delete a student \n")
            print("9. Exit \n")
            user_selection = int(input("Choose an option: "))
            if user_selection not in range(1,10):
                print("Invalid option, please choose a valid option.")
            else:
                return user_selection
        except ValueError as error:
            print(f"Invalid selection, please try again. error details: {error}")
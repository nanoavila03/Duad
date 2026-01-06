def show_menu():
    while True:
        print("\nStudent Control System Menu:")
        print("=====================================")
        print("1. Enter student information")
        print("2. Display all students")
        print("3. Search for a student by name")
        print("4. Calculate average grades and show top 3 subjects")
        print("5. Delete a student by name")
        print("6. Create or Update CSV")
        print("7. Open CSV")
        print("8. Show students who failed")
        print("9. Exit")
        print()
        choice = input("Please select an option (1-9): ")

        if choice in [str(i) for i in range(1, 10)]:
            return choice
        else:
            print()
            print("Invalid option. Please select a number between 1 and 9.")


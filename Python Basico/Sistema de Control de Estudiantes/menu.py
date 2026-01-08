def show_menu():
    while True:
        print("\nStudent Control System Menu:")
        print("=====================================")
        print("1. Enter student information")
        print("2. Display all students")
        print("3. Search for a student by name")
        print("4. Show top 3 students")
        print("5. Delete a student by name")
        print("6. Save CSV")
        print("7. Switch to another CSV file")
        print("8. Show students who failed")
        print("9. Show overall class average")
        print("10. Exit")
        print()
        choice = input("Please select an option (1-10): ")

        if choice in [str(i) for i in range(1, 11)]:
            return choice
        else:
            print()
            print("Invalid option. Please select a number between 1 and 10.")
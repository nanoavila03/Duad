import menu
import actions
import data

def select_csv_file():
    """Function to select or create a CSV file"""
    data.list_csv_files()
    
    file_loaded = False
    while not file_loaded:
        create_or_open = input("Do you want to (1) Create a new CSV file or (2) Open an existing CSV file? Enter 1 or 2: ")
        if create_or_open not in ['1', '2']:
            print("Invalid option. Please enter 1 or 2.")
            continue
        
        if create_or_open == '1':
            file_path = input("Enter the name for the new CSV file (e.g., students.csv): ")
            data.save_students_to_csv(file_path, [])
            print("Empty CSV file created successfully in 'CSV files' folder.")
            students = []
            file_loaded = True
            return file_path, students
        
        else:
            while True:
                file_path = input("Enter the CSV file name to open (e.g., students.csv): ")
                
                if data.file_exists(file_path):
                    students = data.load_students_from_csv(file_path)
                    file_loaded = True
                    return file_path, students
                else:
                    print(f"Error: File '{file_path}' not found in 'CSV files' folder.")
                    retry = input("Do you want to (1) Try again or (2) Create a new file? Enter 1 or 2: ")
                    if retry == '2':
                        break
                    elif retry != '1':
                        print("Invalid option. Returning to file selection...")
                        break

def main():
    print("\n" + "="*50)
    print("STUDENT CONTROL SYSTEM")
    print("="*50)
    
    # Initial file selection
    file_path, students = select_csv_file()

    while True:
        choice = menu.show_menu()

        if choice == '1':
            student = actions.enter_student_info()
            if not actions.validate_student_exists(students, student['Full name']):
                students.append(student)
                print("Student added successfully.")
            else:
                print("Student already exists.")

        elif choice == '2':
            actions.display_students(students)

        elif choice == '3':
            name = input("Enter the full name of the student to search: ")
            actions.search_student_by_name(students, name)

        elif choice == '4':
            actions.top_three_averages(students)

        elif choice == '5':
            name = input("Enter the full name of the student to delete: ")
            students = actions.delete_student_by_name(students, name)

        elif choice == '6':
            data.save_students_to_csv(file_path, students)
            print("CSV file Saved successfully.")

        elif choice == '7':
            print("\n" + "="*50)
            print("SWITCHING CSV FILE")
            print("="*50)
            # Automatically save current file before switching
            data.save_students_to_csv(file_path, students)
            print("Current file saved automatically.")
            
            # Select new file
            file_path, students = select_csv_file()

        elif choice == '8':
            actions.students_disaproved(students)

        elif choice == '9':
            actions.show_overall_average(students)

        elif choice == '10':
            data.save_students_to_csv(file_path, students)
            print("Changes saved automatically.")
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()


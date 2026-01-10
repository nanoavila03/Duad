import menu
import actions
import data

def main():
    print("\nSTUDENT CONTROL SYSTEM")
    
    file_path, students = actions.select_csv_file(data)

    while True:
        menu.show_menu()
        
        choice = input("\nPlease select an option (1-10): ")
        
        if not actions.is_valid_menu_option(choice):
            print("\nInvalid option. Please select a number between 1 and 10.")
            continue

        if choice == '1':
            students = actions.add_student(students)

        elif choice == '2':
            students = actions.display_all_students(students)

        elif choice == '3':
            name = input("Enter the full name of the student to search: ")
            students = actions.search_student_by_name(students, name)

        elif choice == '4':
            students = actions.show_top_three(students)

        elif choice == '5':
            name = input("Enter the full name of the student to delete: ")
            students = actions.delete_student(students, name)

        elif choice == '6':
            data.save_students_to_csv(file_path, students)
            print("CSV file saved successfully.")

        elif choice == '7':
            print("\nSWITCHING CSV FILE")
            data.save_students_to_csv(file_path, students)
            print("Current file saved automatically.")
            
            file_path, students = actions.select_csv_file(data)

        elif choice == '8':
            students = actions.show_failed_students(students)

        elif choice == '9':
            students = actions.show_overall_average(students)

        elif choice == '10':
            data.save_students_to_csv(file_path, students)
            print("Changes saved automatically.")
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
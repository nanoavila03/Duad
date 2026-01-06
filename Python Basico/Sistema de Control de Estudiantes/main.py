import menu 
import actions
import data

def main():
    students = []
    file_path = 'students.csv'
    students = data.load_students_from_csv(file_path)

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
            actions.display_all_students(students)

        elif choice == '3':
            name = input("Enter the full name of the student to search: ")
            actions.search_student_by_name(students, name)

        elif choice == '4':
            actions.calculate_averages_and_top_subjects(students)

        elif choice == '5':
            name = input("Enter the full name of the student to delete: ")
            students = actions.delete_student_by_name(students, name)

        elif choice == '6':
            data.save_students_to_csv(file_path, students)
            print("CSV file created/updated successfully.")

        elif choice == '7':
            students = data.load_students_from_csv(file_path)
            print("CSV file opened successfully.")

        elif choice == '8':
            actions.students_disaproved(students)

        elif choice == '9':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
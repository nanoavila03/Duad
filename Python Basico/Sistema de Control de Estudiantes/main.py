import menu 
import actions
import data

def main():
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
            actions.display_students(students)

        elif choice == '3':
            name = input("Enter the name to search: ")
            actions.search_student_by_name(students, name)

        elif choice == '4':
            actions.top_three_averages(students)

        elif choice == '5':
            name = input("Enter the name of the student to delete: ")
            students = actions.delete_student_by_name(students, name)

        elif choice == '6':
            data.save_students_to_csv(file_path, students)
            print(f"Students saved to {file_path}.")

        elif choice == '7':
            students = data.load_students_from_csv(file_path)
            print(f"Students loaded from {file_path}.")

        elif choice == '8':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
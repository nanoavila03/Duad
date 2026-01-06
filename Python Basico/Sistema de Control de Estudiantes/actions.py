import data
import re

def validate_grade(grade):
    try:
        grade = float(grade)
        if 0 <= grade <= 100:
            return True
        else:
            print("Grade must be between 0 and 100.")
            return False
    except ValueError:
        print("Invalid grade. Please enter a numeric value.")
        return False

def validate_name(name):
    if any(char.isdigit() for char in name):
        print("Invalid name. Names should not contain numbers.")
        return False
    return True

def validate_section(section):
    pattern = r'^\d{1,2}[A-Z]$'
    return bool(re.match(pattern, section)) 

def validate_student_exists(students, name):
    for student in students:
        if name.lower() == student['Full name'].lower():
            return True
    return False

def enter_student_info():
    while True:
        name = input("Enter full name: ")
        if validate_name(name):
            break

    while True:
        section = input("Enter section (e.g., 10A): ")
        if validate_section(section):
            break
        else:
            print("Invalid section format. Please use the format like '10A'.")

    grades = {}
    subjects = ['Spanish', 'English', 'Social Studies', 'Science']
    for subject in subjects:
        while True:
            grade = input(f"Enter {subject} grade (0-100): ")
            if validate_grade(grade):
                grades[f'{subject} grade'] = float(grade)
                break

    student = {
        'Full name': name,
        'Section': section,
        'Spanish grade': grades['Spanish grade'],
        'English grade': grades['English grade'],
        'Social Studies grade': grades['Social Studies grade'],
        'Science grade': grades['Science grade']
    }
    return student

def display_students(students):
    for student in students:
        print(f"Name: {student['Full name']}, Section: {student['Section']}, "
                f"Spanish: {student['Spanish grade']}, English: {student['English grade']}, "
                f"Social Studies: {student['Social Studies grade']}, Science: {student['Science grade']}")
    if not students:
        print("No student records available.")
    return students


def calculate_average_grades_top_3(students):
    if not students:
        print("No student records available to calculate averages.")
        return

    total_spanish = total_english = total_social_studies = total_science = 0
    num_students = len(students)

    for student in students:
        total_spanish += float(student['Spanish grade'])
        total_english += float(student['English grade'])
        total_social_studies += float(student['Social Studies grade'])
        total_science += float(student['Science grade'])

    avg_spanish = total_spanish / num_students
    avg_english = total_english / num_students
    avg_social_studies = total_social_studies / num_students
    avg_science = total_science / num_students

    print(f"Average Spanish Grade: {avg_spanish:.2f}")
    print(f"Average English Grade: {avg_english:.2f}")
    print(f"Average Social Studies Grade: {avg_social_studies:.2f}")
    print(f"Average Science Grade: {avg_science:.2f}")
    return {
        'Spanish': avg_spanish,
        'English': avg_english,
        'Social Studies': avg_social_studies,
        'Science': avg_science
    }


def search_student_by_name(students, name):
    found_students = [student for student in students if name.lower() in student['Full name'].lower()]
    if found_students:
        for student in found_students:
            print(f"Found: Name: {student['Full name']}, Section: {student['Section']}, "
                    f"Spanish: {student['Spanish grade']}, English: {student['English grade']}, "
                    f"Social Studies: {student['Social Studies grade']}, Science: {student['Science grade']}")
    else:
        print(f"No student found with the name containing '{name}'.")
    return found_students

def confirm_deletion(student):
    confirmation = input(f"Are you sure you want to delete {student['Full name']}? (yes/no): ")
    return confirmation.lower() == 'yes'

def delete_student_by_name(students, name):
    for i, student in enumerate(students):
        if name.lower() in student['Full name'].lower():
            if confirm_deletion(student):
                del students[i]
                print(f"Student {student['Full name']} deleted.")
                return students
            else:
                print("Deletion cancelled.")
                return students
    print(f"No student found with the name containing '{name}'.")
    return students

def update_student_info(students, name):
    for student in students:
        if name.lower() in student['Full name'].lower():
            print(f"Updating information for {student['Full name']}:")
            student['Section'] = input(f"Enter new section (current: {student['Section']}): ") or student['Section']
            student['Spanish grade'] = input(f"Enter new Spanish grade (current: {student['Spanish grade']}): ") or student['Spanish grade']
            student['English grade'] = input(f"Enter new English grade (current: {student['English grade']}): ") or student['English grade']
            student['Social Studies grade'] = input(f"Enter new Social Studies grade (current: {student['Social Studies grade']}): ") or student['Social Studies grade']
            student['Science grade'] = input(f"Enter new Science grade (current: {student['Science grade']}): ") or student['Science grade']
            print("Student information updated.")
            return students
    print(f"No student found with the name containing '{name}'.")
    return students

def top_three_averages(students):
    averages = calculate_average_grades_top_3(students)
    if averages:
        sorted_averages = sorted(averages.items(), key=lambda item: item[1], reverse=True)
        print("Top three subjects with highest average grades:")
        for subject, avg in sorted_averages[:3]:
            print(f"{subject}: {avg:.2f}")

    
  
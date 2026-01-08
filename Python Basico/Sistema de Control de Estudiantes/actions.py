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

def validate_student_disapproved(student, passing_grade=60):
    failed_subjects = []
    subjects = ['Spanish grade', 'English grade', 'Social Studies grade', 'Science grade']
    
    for subject in subjects:
        if subject in student and student[subject] < passing_grade:
            failed_subjects.append(subject)
    
    return failed_subjects

def enter_student_info():
    while True:
        name = input("Enter full name: ")
        if validate_name(name):
            break

    while True:
        print("=====================================")
        section = input("Enter section (e.g., 10A): ")
        print("=====================================")
        if validate_section(section):
            break
        else:
            print("=====================================")
            print("Invalid section format. Please use the format like '10A'.")
            print("=====================================")

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
    if not students:
        print("=====================================")
        print("No student records available.")
        print("=====================================")
        return students
    
    for student in students:
        print("=====================================")
        print(f"Name: {student['Full name']}, Section: {student['Section']}, "
                f"Spanish: {student['Spanish grade']}, English: {student['English grade']}, "
                f"Social Studies: {student['Social Studies grade']}, Science: {student['Science grade']}")
    
    print("=====================================")
    return students


def search_student_by_name(students, name):
    found_students = [student for student in students if name.lower() in student['Full name'].lower()]
    if found_students:
        for student in found_students:
            print("=====================================")
            print(f"Found: Name: {student['Full name']}, Section: {student['Section']}, "
                    f"Spanish: {student['Spanish grade']}, English: {student['English grade']}, "
                    f"Social Studies: {student['Social Studies grade']}, Science: {student['Science grade']}")
            print("=====================================")
    else:
        print("=====================================")
        print(f"No student found with the name containing '{name}'.")
        print("=====================================")
    return found_students

def confirm_deletion(student):
    print("=====================================")
    confirmation = input(f"Are you sure you want to delete {student['Full name']}? (yes/no): ")
    print("=====================================")
    return confirmation.lower() == 'yes'

def delete_student_by_name(students, name):
    for i, student in enumerate(students):
        if name.lower() in student['Full name'].lower():
            if confirm_deletion(student):
                del students[i]
                print("=====================================")
                print(f"Student {student['Full name']} deleted.")
                print("=====================================")
                return students
            else:
                print("=====================================")
                print("Deletion cancelled.")
                print("=====================================")
                return students
    print("=====================================")
    print(f"No student found with the name containing '{name}'.")
    print("=====================================")
    return students

def update_student_info(students, name):
    for student in students:
        if name.lower() in student['Full name'].lower():
            print("=====================================")
            print(f"Updating information for {student['Full name']}:")
            
            while True:
                new_section = input(f"Enter new section (current: {student['Section']}, press Enter to keep): ")
                if not new_section:
                    break
                if validate_section(new_section):
                    student['Section'] = new_section
                    break
                else:
                    print("Invalid section format. Please use the format like '10A'.")
            
            subjects = ['Spanish', 'English', 'Social Studies', 'Science']
            for subject in subjects:
                grade_key = f'{subject} grade'
                while True:
                    new_grade = input(f"Enter new {subject} grade (current: {student[grade_key]}, press Enter to keep): ")
                    if not new_grade:
                        break
                    if validate_grade(new_grade):
                        student[grade_key] = float(new_grade)
                        break
            
            print("Student information updated.")
            print("=====================================")
            return students
    
    print("=====================================")    
    print(f"No student found with the name containing '{name}'.")
    print("=====================================")
    return students

def students_disaproved(students, passing_grade=60):
    disapproved_students = []
    for student in students:
        failed_subjects = validate_student_disapproved(student, passing_grade)
        if failed_subjects:
            disapproved_students.append((student, failed_subjects))

    if disapproved_students:
        print("=====================================")
        print("Students who failed:")
        print("=====================================")
        for student, subjects in disapproved_students:
            failed_info = [f"{subj.replace(' grade', '')} ({student[subj]:.1f})" for subj in subjects]
            print(f"Student: {student['Full name']} - Section: {student['Section']}")
            print(f"Failed subjects: {', '.join(failed_info)}")
            print("-------------------------------------")
        print("=====================================")
    else:
        print("=====================================")
        print("No students have failed.")
        print("=====================================")
    return disapproved_students

def calculate_averages_per_student(student):
    subjects = ['Spanish grade', 'English grade', 'Social Studies grade', 'Science grade']
    
    sum_grades = 0
    
    for subject in subjects:
        sum_grades += student[subject]
    
    average = sum_grades / len(subjects)
    
    return average

def top_three_averages(students):
    if not students:
        print("=====================================")
        print("No student records available to calculate averages.")
        print("=====================================")
        return []

    averages = []
    for student in students:
        avg = calculate_averages_per_student(student)
        averages.append((student['Full name'], avg))

    averages.sort(key=lambda x: x[1], reverse=True)
    top_three = averages[:3]

    print("=====================================")
    print("Top 3 Students by Average Grades:")
    print("=====================================")
    for i, (name, avg) in enumerate(top_three, 1):
        print(f"{i}. {name} - Average Grade: {avg:.2f}")
    print("=====================================")
    return top_three

def show_overall_average(students):
    if not students:
        print("=====================================")
        print("No student records available to calculate average.")
        print("=====================================")
        return None
    total_sum = 0

    for student in students:
        student_avg = calculate_averages_per_student(student)
        total_sum += student_avg
    overall_average = total_sum / len(students)
    print("=====================================")
    print(f"Total number of students: {len(students)}")
    print(f"Overall class average: {overall_average:.2f}")
    print("=====================================")
    
    return overall_average
import re


def is_valid_menu_option(choice):
    valid_options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    if choice in valid_options:
        return True
    else:
        return False

def is_valid_grade(grade_str):
    try:
        grade = float(grade_str)
        if grade >= 0 and grade <= 100:
            return True
        else:
            return False
    except ValueError:
        return False

def is_valid_name(name):
    if not name:
        return False
    
    if not name.strip():
        return False
    
    has_digit = False
    for char in name:
        if char.isdigit():
            has_digit = True
            break
    
    if has_digit:
        return False
    else:
        return True

def is_valid_section(section):
    pattern = r'^\d{1,2}[A-Z]$'
    match = re.match(pattern, section)
    if match:
        return True
    else:
        return False

def student_exists(students, name):
    for student in students:
        student_name = student['Full name']
        student_name_lower = student_name.lower()
        name_lower = name.lower()
        
        if student_name_lower == name_lower:
            return True
    
    return False


def input_valid_name():
    while True:
        name = input("Enter full name: ")
        name = name.strip()
        
        if is_valid_name(name):
            return name
        else:
            print("Invalid name. Names should not contain numbers and cannot be empty.")

def input_valid_section():
    while True:
        print()
        section = input("Enter section (e.g., 10A): ")
        section = section.strip()
        
        if is_valid_section(section):
            return section
        else:
            print()
            print("Invalid section format. Please use the format like '10A'.")

def input_valid_grade(subject_name):
    while True:
        prompt = f"Enter {subject_name} grade (0-100): "
        grade_str = input(prompt)
        
        if is_valid_grade(grade_str):
            grade = float(grade_str)
            return grade
        else:
            print("Invalid grade. Please enter a numeric value between 0 and 100.")

def input_optional_section(current_section):
    while True:
        prompt = f"Enter new section (current: {current_section}, press Enter to keep): "
        new_section = input(prompt)
        new_section = new_section.strip()
        
        if not new_section:
            return current_section
        
        if is_valid_section(new_section):
            return new_section
        else:
            print("Invalid section format. Please use the format like '10A'.")

def input_optional_grade(subject_name, current_grade):
    while True:
        prompt = f"Enter new {subject_name} grade (current: {current_grade}, press Enter to keep): "
        grade_str = input(prompt)
        grade_str = grade_str.strip()
        
        if not grade_str:
            return current_grade
        
        if is_valid_grade(grade_str):
            grade = float(grade_str)
            return grade
        else:
            print("Invalid grade. Please enter a numeric value between 0 and 100.")

def select_csv_file(data_module):
    data_module.list_csv_files()
    
    file_loaded = False
    
    while not file_loaded:
        create_or_open = input("Do you want to (1) Create a new CSV file or (2) Open an existing CSV file? Enter 1 or 2: ")
        
        if create_or_open not in ['1', '2']:
            print("Invalid option. Please enter 1 or 2.")
            continue
        
        if create_or_open == '1':
            file_path = input("Enter the name for the new CSV file (e.g., students.csv): ")
            empty_list = []
            data_module.save_students_to_csv(file_path, empty_list)
            print("Empty CSV file created successfully in 'CSV files' folder.")
            students = []
            file_loaded = True
            return file_path, students
        
        else:
            while True:
                file_path = input("Enter the CSV file name to open (e.g., students.csv): ")
                
                file_found = data_module.file_exists(file_path)
                
                if file_found:
                    students = data_module.load_students_from_csv(file_path)
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


def add_student(students):
    name = input_valid_name()
    
    exists = student_exists(students, name)
    if exists:
        print()
        print("Student already exists.")
        return students
    
    section = input_valid_section()
    
    subjects = ['Spanish', 'English', 'Social Studies', 'Science']
    grades = {}
    
    for subject in subjects:
        grade = input_valid_grade(subject)
        grade_key = f'{subject} grade'
        grades[grade_key] = grade
    
    student = {
        'Full name': name,
        'Section': section,
        'Spanish grade': grades['Spanish grade'],
        'English grade': grades['English grade'],
        'Social Studies grade': grades['Social Studies grade'],
        'Science grade': grades['Science grade']
    }
    
    students.append(student)
    print()
    print("Student added successfully.")
    return students

def display_all_students(students):
    if not students:
        print()
        print("No student records available.")
        return students
    
    for student in students:
        name = student['Full name']
        section = student['Section']
        spanish = student['Spanish grade']
        english = student['English grade']
        social = student['Social Studies grade']
        science = student['Science grade']
        
        print(f"Name: {name}, Section: {section}, Spanish: {spanish}, English: {english}, Social Studies: {social}, Science: {science}")
    
    return students

def search_student_by_name(students, name):
    found_students = []
    name_lower = name.lower()
    
    for student in students:
        student_name = student['Full name']
        student_name_lower = student_name.lower()
        
        if name_lower in student_name_lower:
            found_students.append(student)
    
    if found_students:
        for student in found_students:
            name = student['Full name']
            section = student['Section']
            spanish = student['Spanish grade']
            english = student['English grade']
            social = student['Social Studies grade']
            science = student['Science grade']
            
            print(f"Found: Name: {name}, Section: {section}, Spanish: {spanish}, English: {english}, Social Studies: {social}, Science: {science}")
    else:
        print()
        print(f"No student found with the name containing '{name}'.")
    
    return students

def delete_student(students, name):
    name_lower = name.lower()
    
    for i in range(len(students)):
        student = students[i]
        student_name = student['Full name']
        student_name_lower = student_name.lower()
        
        if name_lower in student_name_lower:
            prompt = f"Are you sure you want to delete {student_name}? (yes/no): "
            confirmation = input(prompt)
            
            if confirmation.lower() == 'yes':
                del students[i]
                print(f"Student {student_name} deleted.")
                return students
            else:
                print("Deletion cancelled.")
                return students
    
    print(f"No student found with the name containing '{name}'.")
    return students

def update_student(students, name):
    name_lower = name.lower()
    
    for student in students:
        student_name = student['Full name']
        student_name_lower = student_name.lower()
        
        if name_lower in student_name_lower:
            print(f"Updating information for {student_name}:")
            
            current_section = student['Section']
            new_section = input_optional_section(current_section)
            student['Section'] = new_section
            
            subjects = ['Spanish', 'English', 'Social Studies', 'Science']
            for subject in subjects:
                grade_key = f'{subject} grade'
                current_grade = student[grade_key]
                new_grade = input_optional_grade(subject, current_grade)
                student[grade_key] = new_grade
            
            print("Student information updated.")
            return students
    
    print()
    print(f"No student found with the name containing '{name}'.")
    return students

def show_top_three(students):
    if not students:
        print()
        print("No student records available to calculate averages.")
        return students
    
    averages = []
    
    for student in students:
        spanish = student['Spanish grade']
        english = student['English grade']
        social = student['Social Studies grade']
        science = student['Science grade']
        
        total = spanish + english + social + science
        avg = total / 4
        
        student_name = student['Full name']
        averages.append((student_name, avg))
    
    averages.sort(key=lambda x: x[1], reverse=True)
    
    top_three = averages[:3]
    
    print("Top 3 Students by Average Grades:")
    rank = 1
    for name, avg in top_three:
        print(f"{rank}. {name} - Average Grade: {avg:.2f}")
        rank = rank + 1
    
    return students

def show_overall_average(students):
    if not students:
        print()
        print("No student records available to calculate average.")
        return students
    
    total_sum = 0
    
    for student in students:
        spanish = student['Spanish grade']
        english = student['English grade']
        social = student['Social Studies grade']
        science = student['Science grade']
        
        student_total = spanish + english + social + science
        student_avg = student_total / 4
        total_sum = total_sum + student_avg
    
    student_count = len(students)
    overall_average = total_sum / student_count
    
    print(f"Total number of students: {student_count}")
    print(f"Overall class average: {overall_average:.2f}")
    
    return students

def show_failed_students(students, passing_grade=60):
    failed_students = []
    
    for student in students:
        failed_subjects = []
        
        spanish = student['Spanish grade']
        if spanish < passing_grade:
            failed_subjects.append('Spanish grade')
        
        english = student['English grade']
        if english < passing_grade:
            failed_subjects.append('English grade')
        
        social = student['Social Studies grade']
        if social < passing_grade:
            failed_subjects.append('Social Studies grade')
        
        science = student['Science grade']
        if science < passing_grade:
            failed_subjects.append('Science grade')
        
        if failed_subjects:
            failed_students.append((student, failed_subjects))
    
    if failed_students:
        print()
        print("Students who failed:")
        
        for student, subjects in failed_students:
            student_name = student['Full name']
            student_section = student['Section']
            
            failed_info = []
            for subj in subjects:
                subject_name = subj.replace(' grade', '')
                grade = student[subj]
                info = f"{subject_name} ({grade:.1f})"
                failed_info.append(info)
            
            failed_text = ', '.join(failed_info)
            
            print(f"Student: {student_name} - Section: {student_section}")
            print(f"Failed subjects: {failed_text}")
    else:
        print()
        print("No students have failed.")
    
    return students
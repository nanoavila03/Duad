import re

def is_valid_menu_option(choice):
    return choice in [str(i) for i in range(1, 11)]

def is_valid_grade(grade_str):
    try:
        grade = float(grade_str)
        return 0 <= grade <= 100
    except ValueError:
        return False

def is_valid_name(name):
    if not name or not name.strip():
        return False
    return not any(char.isdigit() for char in name)

def is_valid_section(section):
    pattern = r'^\d{1,2}[A-Z]$'
    return bool(re.match(pattern, section))

def student_exists(students, name):
    for student in students:
        if name.lower() == student['Full name'].lower():
            return True
    return False



def input_valid_name():
    while True:
        name = input("Enter full name: ").strip()
        if is_valid_name(name):
            return name
        print("Invalid name. Names should not contain numbers and cannot be empty.")

def input_valid_section():
    while True:
        section = input("\nEnter section (e.g., 10A): ").strip()
        if is_valid_section(section):
            return section
        print("\nInvalid section format. Please use the format like '10A'.")

def input_valid_grade(subject_name):
    while True:
        grade_str = input(f"Enter {subject_name} grade (0-100): ")
        if is_valid_grade(grade_str):
            return float(grade_str)
        print("Invalid grade. Please enter a numeric value between 0 and 100.")

def input_optional_section(current_section):
    while True:
        new_section = input(f"Enter new section (current: {current_section}, press Enter to keep): ").strip()
        if not new_section:
            return current_section
        if is_valid_section(new_section):
            return new_section
        print("Invalid section format. Please use the format like '10A'.")

def input_optional_grade(subject_name, current_grade):
    while True:
        grade_str = input(f"Enter new {subject_name} grade (current: {current_grade}, press Enter to keep): ").strip()
        if not grade_str:
            return current_grade
        if is_valid_grade(grade_str):
            return float(grade_str)
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
            data_module.save_students_to_csv(file_path, [])
            print("Empty CSV file created successfully in 'CSV files' folder.")
            students = []
            file_loaded = True
            return file_path, students
        
        else:
            while True:
                file_path = input("Enter the CSV file name to open (e.g., students.csv): ")
                
                if data_module.file_exists(file_path):
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
    
    if student_exists(students, name):
        print("\nStudent already exists.")
        return students
    
    section = input_valid_section()
    
    subjects = ['Spanish', 'English', 'Social Studies', 'Science']
    grades = {}
    for subject in subjects:
        grades[f'{subject} grade'] = input_valid_grade(subject)
    
    student = {
        'Full name': name,
        'Section': section,
        'Spanish grade': grades['Spanish grade'],
        'English grade': grades['English grade'],
        'Social Studies grade': grades['Social Studies grade'],
        'Science grade': grades['Science grade']
    }
    
    students.append(student)
    print("\nStudent added successfully.")
    return students

def display_all_students(students):
    if not students:
        print("\nNo student records available.")
        return students
    
    for student in students:
        print(f"Name: {student['Full name']}, Section: {student['Section']}, "
              f"Spanish: {student['Spanish grade']}, English: {student['English grade']}, "
              f"Social Studies: {student['Social Studies grade']}, Science: {student['Science grade']}")
    
    return students

def search_student_by_name(students, name):
    found_students = [student for student in students if name.lower() in student['Full name'].lower()]
    
    if found_students:
        for student in found_students:
            print(f"Found: Name: {student['Full name']}, Section: {student['Section']}, "
                  f"Spanish: {student['Spanish grade']}, English: {student['English grade']}, "
                  f"Social Studies: {student['Social Studies grade']}, Science: {student['Science grade']}")
    else:
        print(f"\nNo student found with the name containing '{name}'.")
    
    return students

def delete_student(students, name):
    for i, student in enumerate(students):
        if name.lower() in student['Full name'].lower():
            confirmation = input(f"Are you sure you want to delete {student['Full name']}? (yes/no): ")
            
            if confirmation.lower() == 'yes':
                del students[i]
                print(f"Student {student['Full name']} deleted.")
                return students
            else:
                print("Deletion cancelled.")
                return students
    
    print(f"No student found with the name containing '{name}'.")
    return students

def update_student(students, name):
    for student in students:
        if name.lower() in student['Full name'].lower():
            print(f"Updating information for {student['Full name']}:")
            
            student['Section'] = input_optional_section(student['Section'])
            
            subjects = ['Spanish', 'English', 'Social Studies', 'Science']
            for subject in subjects:
                grade_key = f'{subject} grade'
                student[grade_key] = input_optional_grade(subject, student[grade_key])
            
            print("Student information updated.")
            return students
    
    print(f"\nNo student found with the name containing '{name}'.")
    return students

def show_top_three(students):
    if not students:
        print("\nNo student records available to calculate averages.")
        return students
    
    averages = []
    for student in students:
        subjects = ['Spanish grade', 'English grade', 'Social Studies grade', 'Science grade']
        total = sum(student[subject] for subject in subjects)
        avg = total / len(subjects)
        averages.append((student['Full name'], avg))
    
    averages.sort(key=lambda x: x[1], reverse=True)
    top_three = averages[:3]
    
    print("Top 3 Students by Average Grades:")
    for i, (name, avg) in enumerate(top_three, 1):
        print(f"{i}. {name} - Average Grade: {avg:.2f}")
    
    return students

def show_overall_average(students):
    if not students:
        print("\nNo student records available to calculate average.")
        return students
    
    total_sum = 0
    for student in students:
        subjects = ['Spanish grade', 'English grade', 'Social Studies grade', 'Science grade']
        student_avg = sum(student[subject] for subject in subjects) / len(subjects)
        total_sum += student_avg
    
    overall_average = total_sum / len(students)
    
    print("=====================================")
    print(f"Total number of students: {len(students)}")
    print(f"Overall class average: {overall_average:.2f}")
    print("=====================================")
    
    return students

def show_failed_students(students, passing_grade=60):
    failed_students = []
    
    for student in students:
        failed_subjects = []
        subjects = ['Spanish grade', 'English grade', 'Social Studies grade', 'Science grade']
        
        for subject in subjects:
            if subject in student and student[subject] < passing_grade:
                failed_subjects.append(subject)
        
        if failed_subjects:
            failed_students.append((student, failed_subjects))
    
    if failed_students:
        print("\nStudents who failed:")
        for student, subjects in failed_students:
            failed_info = [f"{subj.replace(' grade', '')} ({student[subj]:.1f})" for subj in subjects]
            print(f"Student: {student['Full name']} - Section: {student['Section']}")
            print(f"Failed subjects: {', '.join(failed_info)}")
    else:
        print("\nNo students have failed.")    
    return students
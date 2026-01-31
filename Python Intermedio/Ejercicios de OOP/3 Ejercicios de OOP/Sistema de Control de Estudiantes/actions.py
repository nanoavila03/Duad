import re

class Student:
    def __init__(self, full_name, section, spanish_grade, english_grade, social_studies_grade, science_grade):
        self.full_name = full_name
        self.section = section
        self.spanish_grade = float(spanish_grade)
        self.english_grade = float(english_grade)
        self.social_studies_grade = float(social_studies_grade)
        self.science_grade = float(science_grade)
    
    def calculate_average(self):
        return (self.spanish_grade + self.english_grade + self.social_studies_grade + self.science_grade) / 4
    
    def to_dict(self):
        return {
            'Full name': self.full_name, 'Section': self.section,
            'Spanish grade': self.spanish_grade, 'English grade': self.english_grade,
            'Social Studies grade': self.social_studies_grade, 'Science grade': self.science_grade
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            full_name=data['Full name'], section=data['Section'],
            spanish_grade=data['Spanish grade'], english_grade=data['English grade'],
            social_studies_grade=data['Social Studies grade'], science_grade=data['Science grade']
        )
    
    def __str__(self):
        return f"Name: {self.full_name} | Section: {self.section} | Average: {self.calculate_average():.2f}"

def is_valid_menu_option(choice):
    return choice in [str(i) for i in range(1, 11)]

def is_valid_name(name):
    return bool(name.strip()) and not any(char.isdigit() for char in name)

def is_valid_section(section):
    return re.match(r'^\d{1,2}[A-Z]$', section.upper()) is not None

def select_csv_file(data_module):
    data_module.list_csv_files()
    while True:
        op = input("\n(1) Create New (2) Open Existing: ")
        path = input("File name (e.g., students.csv): ")
        
        if op == '1':
            data_module.save_students_to_csv(path, [])
            return path, []
        elif op == '2' and data_module.file_exists(path):
            raw_data = data_module.load_students_from_csv(path)
            students = [Student.from_dict(d) for d in raw_data]
            return path, students
        print("Invalid file or option.")

def add_student(students):
    name = input("Full Name: ")
    if not is_valid_name(name): return students
    
    section = input("Section (e.g. 10A): ").upper()
    if not is_valid_section(section): return students
    
    new_s = Student(name, section, input("Spanish: "), input("English: "), 
                    input("Social: "), input("Science: "))
    students.append(new_s)
    print("Student added.")
    return students

def display_all_students(students):
    if not students: print("No records."); return students
    for s in students: print(s) 
    return students

def show_top_three(students):
    if not students: return students
    top = sorted(students, key=lambda s: s.calculate_average(), reverse=True)[:3]
    print("\n--- TOP 3 ---")
    for i, s in enumerate(top, 1):
        print(f"{i}. {s.full_name}: {s.calculate_average():.2f}")
    return students

def show_failed_students(students):
    failed = [s for s in students if s.calculate_average() < 60]
    if not failed: print("No failed students.")
    for s in failed: print(f"Failed: {s.full_name} ({s.calculate_average():.2f})")
    return students

def show_overall_average(students):
    if not students: return students
    total = sum(s.calculate_average() for s in students)
    print(f"Overall Class Average: {total/len(students):.2f}")
    return students

def search_student_by_name(students, name):
    found = [s for s in students if name.lower() in s.full_name.lower()]
    for s in found: print(s)
    return students

def delete_student(students, name):
    new_list = [s for s in students if s.full_name.lower() != name.lower()]
    if len(new_list) < len(students): print("Student deleted.")
    return new_list
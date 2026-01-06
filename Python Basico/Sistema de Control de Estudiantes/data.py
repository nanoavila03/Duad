import csv
import os

def load_students_from_csv(file_path):
    students = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, file_path)
    
    try:
        with open(full_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                student = {
                    'Full name': row['Full name'],
                    'Section': row['Section'],
                    'Spanish grade': float(row['Spanish grade']),
                    'English grade': float(row['English grade']),
                    'Social Studies grade': float(row['Social Studies grade']),
                    'Science grade': float(row['Science grade'])
                }
                students.append(student)
        print(f"✓ File loaded from: {full_path}")
    except FileNotFoundError:
        print(f"File {file_path} not found. Starting with an empty student list.")
    return students

def save_students_to_csv(file_path, students):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, file_path)
    
    with open(full_path, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Full name', 'Section', 'Spanish grade', 'English grade', 'Social Studies grade', 'Science grade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)
    
    print(f"File saved at: {full_path}")

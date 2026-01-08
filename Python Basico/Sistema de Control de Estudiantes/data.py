import csv
import os

CSV_FOLDER = "CSV files"

def ensure_csv_extension(file_path):
    if not file_path.endswith('.csv'):
        return file_path + '.csv'
    return file_path

def get_full_path(file_path):
    file_path = ensure_csv_extension(file_path)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_folder = os.path.join(script_dir, CSV_FOLDER)
    return os.path.join(csv_folder, file_path)

def list_csv_files():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_folder = os.path.join(script_dir, CSV_FOLDER)
    
    try:
        csv_files = [f for f in os.listdir(csv_folder) if f.endswith('.csv')]
        
        if csv_files:
            print("=====================================")
            print("Available CSV files:")
            for i, file in enumerate(csv_files, 1):
                print(f"  {i}. {file}")
            print("=====================================")
        else:
            print("=====================================")
            print("No CSV files found in the student_data folder.")
            print("=====================================")
        
        return csv_files
    except Exception as e:
        print(f"Error listing files: {e}")
        return []

def file_exists(file_path):
    full_path = get_full_path(file_path)
    return os.path.exists(full_path)

def load_students_from_csv(file_path):
    students = []
    full_path = get_full_path(file_path)
    
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
        print(f"✗ File '{file_path}' not found in student_data folder.")
    except Exception as e:
        print(f"✗ Error loading file: {e}")
    return students

def save_students_to_csv(file_path, students):
    full_path = get_full_path(file_path)
    
    try:
        with open(full_path, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Full name', 'Section', 'Spanish grade', 'English grade', 'Social Studies grade', 'Science grade']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                writer.writerow(student)
        
        print(f"✓ File saved at: {full_path}")
    except Exception as e:
        print(f"✗ Error saving file: {e}")
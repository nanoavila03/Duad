import csv
import os

CSV_FOLDER = "CSV files"

def get_full_path(file_path):
    if not file_path.endswith('.csv'):
        file_path += '.csv'
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_folder = os.path.join(script_dir, CSV_FOLDER)
    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)
    return os.path.join(csv_folder, file_path)

def list_csv_files():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_folder = os.path.join(script_dir, CSV_FOLDER)
    try:
        if not os.path.exists(csv_folder): return []
        files = [f for f in os.listdir(csv_folder) if f.endswith('.csv')]
        if files:
            print("\nAvailable CSV files:")
            for i, f in enumerate(files, 1):
                print(f"  {i}. {f}")
        return files
    except Exception: return []

def file_exists(file_path):
    return os.path.exists(get_full_path(file_path))

def load_students_from_csv(file_path):
    students_data = []
    full_path = get_full_path(file_path)
    try:
        with open(full_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                students_data.append(row)
    except Exception: pass
    return students_data

def save_students_to_csv(file_path, students):
    full_path = get_full_path(file_path)
    try:
        with open(full_path, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Full name', 'Section', 'Spanish grade', 'English grade', 'Social Studies grade', 'Science grade']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                writer.writerow(student.to_dict())
    except Exception as e:
        print(f"Error saving: {e}")     
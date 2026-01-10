import csv
import os

CSV_FOLDER = "CSV files"

def ensure_csv_extension(file_path):
    has_extension = file_path.endswith('.csv')
    
    if not has_extension:
        file_path = file_path + '.csv'
        return file_path
    else:
        return file_path

def get_full_path(file_path):
    file_path = ensure_csv_extension(file_path)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_folder = os.path.join(script_dir, CSV_FOLDER)
    full_path = os.path.join(csv_folder, file_path)
    
    return full_path

def list_csv_files():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_folder = os.path.join(script_dir, CSV_FOLDER)
    
    try:
        all_files = os.listdir(csv_folder)
        
        csv_files = []
        for f in all_files:
            if f.endswith('.csv'):
                csv_files.append(f)
        
        if csv_files:
            print("\nAvailable CSV files:")
            
            counter = 1
            for file in csv_files:
                print(f"  {counter}. {file}")
                counter = counter + 1
            
        else:
            print("\nNo CSV files found in the CSV files folder.")
        
        return csv_files
        
    except Exception as e:
        print(f"\nError listing files: {e}")
        empty_list = []
        return empty_list

def file_exists(file_path):
    full_path = get_full_path(file_path)
    exists = os.path.exists(full_path)
    return exists

def load_students_from_csv(file_path):
    students = []
    full_path = get_full_path(file_path)
    
    try:
        csvfile = open(full_path, mode='r', newline='', encoding='utf-8')
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            full_name = row['Full name']
            section = row['Section']
            spanish_grade = float(row['Spanish grade'])
            english_grade = float(row['English grade'])
            social_grade = float(row['Social Studies grade'])
            science_grade = float(row['Science grade'])
            
            student = {
                'Full name': full_name,
                'Section': section,
                'Spanish grade': spanish_grade,
                'English grade': english_grade,
                'Social Studies grade': social_grade,
                'Science grade': science_grade
            }
            
            students.append(student)
        
        csvfile.close()
        print(f"\n File loaded from: {full_path}")
        
    except FileNotFoundError:
        print(f"\n File '{file_path}' not found in CSV files folder.")
    except Exception as e:
        print(f"\n Error loading file: {e}")
    
    return students

def save_students_to_csv(file_path, students):
    full_path = get_full_path(file_path)
    
    try:
        csvfile = open(full_path, mode='w', newline='', encoding='utf-8')
        
        fieldnames = ['Full name', 'Section', 'Spanish grade', 'English grade', 'Social Studies grade', 'Science grade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for student in students:
            writer.writerow(student)
        
        csvfile.close()
        print(f"\n File saved at: {full_path}")
        
    except Exception as e:
        print(f"\n Error saving file: {e}")
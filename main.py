import os
import pandas as pd

# Data Read in CSV 
def extract_data_from_csv(csv_path):
    df = pd.read_csv(csv_path)
    employee_data = dict(zip(df['EmployeeID'], df['Email']))
    return employee_data

# Get PDF Filenames with full paths
def get_pdf_filenames(pdf_folder):
    pdf_files = []
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            full_path = os.path.join(pdf_folder, filename)
            filename_without_ext = filename.replace('.pdf', '')
            pdf_files.append({
                'name': filename_without_ext,
                'path': full_path
            })
    return pdf_files

# Find Matching PDFs
def find_matching_pdfs(employee_data, pdf_files):
    matching_pdfs = {}
    
    for emp_id in employee_data.keys():
        for pdf_file in pdf_files:
            if emp_id in pdf_file['name']:
                matching_pdfs[emp_id] = {
                    'filename': pdf_file['name'],
                    'path': pdf_file['path'],
                    'email': employee_data[emp_id]
                }
    
    return matching_pdfs

def find_missing_pdfs(employee_data, matching_pdfs):
    missing_pdfs = []
    for emp_id in employee_data.keys():
        if emp_id not in matching_pdfs:
            missing_pdfs.append({
                'employee_id': emp_id,
                'email': employee_data[emp_id]
            })
    return missing_pdfs

# Find Unmatched PDFs
def find_unmatched_pdfs(pdf_files, matching_pdfs):
    matched_filenames = [info['filename'] for info in matching_pdfs.values()]
    unmatched_pdfs = [
        {'name': pdf_file['name'], 'path': pdf_file['path']}
        for pdf_file in pdf_files 
        if pdf_file['name'] not in matched_filenames
    ]
    return unmatched_pdfs

def main(csv_path, pdf_folder):
    # Get data
    employee_data = extract_data_from_csv(csv_path)
    pdf_files = get_pdf_filenames(pdf_folder)
    
    # Find matches and mismatches
    matching_pdfs = find_matching_pdfs(employee_data, pdf_files)
    missing_pdfs = find_missing_pdfs(employee_data, matching_pdfs)
    unmatched_pdfs = find_unmatched_pdfs(pdf_files, matching_pdfs)
    
    # Print results
    print("\nMatching PDFs Found:")
    for emp_id, info in matching_pdfs.items():
        print(f"EmployeeID: {emp_id}")
        print(f"  Filename: {info['filename']}")
        print(f"  Path: {info['path']}")
        print(f"  Email: {info['email']}")
        print()
    
    print("\nEmployees Missing PDFs:")
    if missing_pdfs:
        for employee in missing_pdfs:
            print(f"EmployeeID: {employee['employee_id']}")
            print(f"  Email: {employee['email']}")
            print()
    else:
        print("None")
    
    print("\nUnmatched PDFs (no corresponding employee):")
    if unmatched_pdfs:
        for pdf in unmatched_pdfs:
            print(f"Filename: {pdf['name']}")
            print(f"Path: {pdf['path']}")
            print()
    else:
        print("None")

if __name__ == "__main__":
    CSV_PATH = 'Data/employee.csv'
    PDF_FOLDER = 'Data/PDF'
    
    main(CSV_PATH, PDF_FOLDER)
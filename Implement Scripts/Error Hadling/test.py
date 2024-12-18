import os
import pandas as pd

# Data Read in CSV 
def extract_data_from_csv(csv_path):
    df = pd.read_csv(csv_path)
    employee_data = dict(zip(df['EmployeeID'], df['Email']))
    return employee_data

# Get PDF Filenames
def get_pdf_filenames(pdf_folder):
    pdf_files = []
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            filename_without_ext = filename.replace('.pdf', '')
            pdf_files.append(filename_without_ext)
    return pdf_files

# Find Matching PDFs
def find_matching_pdfs(employee_data, pdf_names):
    matching_pdfs = {}
    
    for emp_id in employee_data.keys():
        for filename in pdf_names:
            if emp_id in filename:
                matching_pdfs[emp_id] = {
                    'filename': filename,
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
def find_unmatched_pdfs(pdf_names, matching_pdfs):
    matched_filenames = [info['filename'] for info in matching_pdfs.values()]
    unmatched_pdfs = [filename for filename in pdf_names if filename not in matched_filenames]
    return unmatched_pdfs

def main(csv_path, pdf_folder):
    # Get data
    employee_data = extract_data_from_csv(csv_path)
    pdf_names = get_pdf_filenames(pdf_folder)
    
    # Find matches and mismatches
    matching_pdfs = find_matching_pdfs(employee_data, pdf_names)
    missing_pdfs = find_missing_pdfs(employee_data, matching_pdfs)
    unmatched_pdfs = find_unmatched_pdfs(pdf_names, matching_pdfs)
    
    # Print results
    print("\nMatching PDFs Found:")
    for emp_id, info in matching_pdfs.items():
        print(f"EmployeeID: {emp_id}")
        print(f"  Filename: {info['filename']}")
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
            print(f"Filename: {pdf}")
    else:
        print("None")

if __name__ == "__main__":
    CSV_PATH = 'Data/employee.csv'
    PDF_FOLDER = 'Data/PDF'
    
    main(CSV_PATH, PDF_FOLDER)
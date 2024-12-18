import os
import pandas as pd

def extract_data_from_csv(csv_path):
    df = pd.read_csv(csv_path)
    employee_data = dict(zip(df['EmployeeID'], df['Email']))
    return employee_data

def get_pdf_filenames(pdf_folder):
    pdf_files = []
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            filename_without_ext = filename.replace('.pdf', '')
            pdf_files.append(filename_without_ext)
    return pdf_files
    
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

def main(csv_path, pdf_folder):
    employee_data = extract_data_from_csv(csv_path)
    pdf_names = get_pdf_filenames(pdf_folder)
    matching_pdfs = find_matching_pdfs(employee_data, pdf_names)
    
    print("Matching PDFs Found:")
    for emp_id, info in matching_pdfs.items():
        print(f"EmployeeID: {emp_id}")
        print(f"  Filename: {info['filename']}")
        print(f"  Email: {info['email']}")
        print()
    

if __name__ == "__main__":
    CSV_PATH = 'Data/employee.csv'
    PDF_FOLDER = 'Data/PDF'
    
    main(CSV_PATH, PDF_FOLDER)
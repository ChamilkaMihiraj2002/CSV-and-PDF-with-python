import pandas as pd

def extract_data_from_csv(csv_path):
    df = pd.read_csv(csv_path)
    employee_data = dict(zip(df['EmployeeID'], df['Email']))
    return employee_data

employee_data = extract_data_from_csv('Data/employee.csv')
print(employee_data)
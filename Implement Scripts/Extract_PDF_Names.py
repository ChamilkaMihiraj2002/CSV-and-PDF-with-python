import os

def get_pdf_filenames(pdf_folder):
    pdf_files = []
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            filename_without_ext = filename.replace('.pdf', '')
            pdf_files.append(filename_without_ext)
    return pdf_files

pdf_names = get_pdf_filenames('Data/PDF')
print(pdf_names)
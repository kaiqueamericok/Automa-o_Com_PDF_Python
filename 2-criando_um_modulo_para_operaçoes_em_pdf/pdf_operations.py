import PyPDF2 as pdf
from PyPDF2 import PdfReader

def get_pdf_metadata(pdf_path):
    with open(pdf_path, 'rb') as f: 
        reader = PdfReader(f)
        info = reader.metadata 
    return info 

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as f: 
        reader = PdfReader(f)
        results = []
        for i in range(0, len(reader.pages)):
            selected_page = reader.pages[i]
            text =  selected_page.extract_text()
            results.append(text)
        return ''.join(results)
    _
# 1- Buscando Dados e Metadados de um Arquivo PDf
print(get_pdf_metadata('files/test_pdf.pdf'))
print(get_pdf_metadata('files/exemplo.pdf'))
print(extract_text_from_pdf('files/test_pdf.pdf'))  
print(extract_text_from_pdf('files/exemplo.pdf'))  



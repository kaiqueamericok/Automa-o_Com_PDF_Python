import PyPDF2 as pdf
from PyPDF2 import PdfReader, PdfWriter
import os


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
        return ' '.join(results)

def split_pdf(pdf_path):
    with open(pdf_path, 'rb') as f: 
        reader = PdfReader(f)
        for page_num in range(0, len(reader.pages)):
            selected_page = reader.pages[page_num]
            writer = PdfWriter() 
            writer.add_page(selected_page)
            # print(os.path.split(pdf_path)[1])
            filename = os.path.split(pdf_path)[1]
            new_filename = f'files/{filename}_{page_num+1}.pdf'

            with open(new_filename, 'wb') as out: 
                writer.write(out) 
            print(f'PDF criado com o nome: {new_filename}') 

def split_pdf_page(pdf_path,start_page:int=0, stop_page:int=0):
    with(open(pdf_path, 'rb')) as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        for page_num in range(start_page, stop_page):
            selected_page = reader.pages[page_num]
            writer.add_page(selected_page)
            filename = os.path.split(pdf_path)[1]
            #print(start_page)
            #print(stop_page)
            new_filename = f'files/{filename}_from_{start_page+1}_to_{stop_page+1}.pdf'
            with open(new_filename, 'wb') as out: 
                writer.write(out)
            




    
    
     
# 1- Buscando Dados e Metadados de um Arquivo PDf
#print(get_pdf_metadata('files/test_pdf.pdf'))
#print(get_pdf_metadata('files/exemplo.pdf'))
#print(extract_text_from_pdf('files/test_pdf.pdf'))  
#print(extract_text_from_pdf('files/.pdf'))

# 2 - Dividindo PDF por página 
#split_pdf('files/exemplo.pdf')  

# 3 Dividindo PDF por página Selecionada
split_pdf_page('files/exemplo.pdf', 0, 2)

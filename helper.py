from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup
import requests
import io

def split_text_documents(docs: list):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    documents = text_splitter.split_documents(docs)
    return documents

def text_to_doc_splitter(text: str):
    doc_splitter = RecursiveCharacterTextSplitter(chunk_size = 10000, chunk_overlap  = 100, length_function = len, add_start_index = True,)
    document = doc_splitter.create_documents([text])
    return document

def load_pdf(pdf):
    pdf_reader = PdfReader(io.BytesIO(pdf))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    document = text_to_doc_splitter(text)
    return document

def extract_text_from_url(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, features="html.parser")
    text = []
    for lines in soup.findAll('div', {'class': 'description__text'}):
        text.append(lines.get_text())
    
    lines = (line.strip() for line in text)
    text = '\n'.join(line for line in lines if line)
    
    document = text_to_doc_splitter(text)
    return document
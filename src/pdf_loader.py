# src/pdf_loader.py
import os
from langchain.document_loaders import UnstructuredPDFLoader

def load_pdfs_from_folder(pdf_folder_path):
    loaders = [UnstructuredPDFLoader(os.path.join(pdf_folder_path, fn)) for fn in os.listdir(pdf_folder_path)]
    return loaders

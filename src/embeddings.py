# src/embeddings.py
from langchain.embeddings import HuggingFaceEmbeddings

# Initialize Hugging Face embeddings
def get_embeddings():
    return HuggingFaceEmbeddings()

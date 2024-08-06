# src/index_creator.py
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from src.embeddings import get_embeddings

def create_index(loaders):
    embeddings = get_embeddings()
    index = VectorstoreIndexCreator(
        embedding=embeddings,
        text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    ).from_loaders(loaders)
    return index

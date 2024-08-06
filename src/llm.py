# src/llm.py
from langchain_community.llms import HuggingFaceEndpoint

def get_llm():
    return HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.2", temperature=0.1, max_length=512)

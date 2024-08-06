# src/qa_chain.py
from langchain.chains import RetrievalQA
from src.llm import get_llm

def create_qa_chain(index):
    llm = get_llm()
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=index.vectorstore.as_retriever(),
        input_key="question"
    )
    return chain

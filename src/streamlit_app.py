# src/streamlit_app.py
# from huggingface_hub import login
# login()

import streamlit as st
import os
import warnings
warnings.filterwarnings('ignore')
from src.text_utils import wrap_text_preserve_newlines, clean_response
from src.pdf_loader import load_pdfs_from_folder
from src.index_creator import create_index
from src.qa_chain import create_qa_chain

# Streamlit UI
st.title("Question Answering with PDFs 📄")
with st.expander("About the App"):
    st.markdown(
        """
        This is a Generative AI powered Question and Answering app that responds to questions about your PDF File.
        """
    )

pdf_folder_path = 'data/pdfs/'

@st.cache_resource
def load_and_create_index(pdf_folder_path):
    if not os.path.exists(pdf_folder_path):
        return None, None
    
    loaders = load_pdfs_from_folder(pdf_folder_path)
    index = create_index(loaders)
    return loaders, index

loaders, index = load_and_create_index(pdf_folder_path)

if loaders is None or index is None:
    st.write(f"Directory '{pdf_folder_path}' not found.")
else:
    @st.cache_resource
    def load_qa_chain(_index):
        return create_qa_chain(_index)

    chain = load_qa_chain(index)

    question = st.text_input("Enter your question:")

    if st.button("Get Answer"):
        if question:
            answer = chain.run(question)
            # wrapped_answer = wrap_text_preserve_newlines(answer)
            clean_answer = clean_response(answer)
            st.write("### Question:")
            st.write(question)
            st.write("### Answer:")
            st.write(clean_answer)
        else:
            st.write("Please enter a question.")
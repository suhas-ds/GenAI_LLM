# Question Answering System with PDFs

This project is a question answering system using Hugging Face's RAG, PDF processing, and a Streamlit web application.

## Directory Structure

- `data/`: Contains PDF files.
- `src/`: Contains source code modules.
  - `text_utils.py`: Utility functions for text processing.
  - `embeddings.py`: Functions for loading Hugging Face embeddings.
  - `pdf_loader.py`: Functions for loading PDF files.
  - `index_creator.py`: Functions for creating the index.
  - `llm.py`: Functions for initializing the language model.
  - `qa_chain.py`: Functions for creating the QA chain.
  - `streamlit_app.py`: Streamlit application.
- `requirements.txt`: List of dependencies.
- `README.md`: Project documentation.

## Installation

1. Install the dependencies:

```bash
pip install -r requirements.txt

#!/bin/bash

python config/hf_login.py

# Run the Streamlit app
python -m streamlit run src/streamlit_app.py

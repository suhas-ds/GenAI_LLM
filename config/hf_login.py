# src/hf_login.py
from huggingface_hub._login import _login
_login(token='YOUR TOKEN', add_to_git_credential=False)
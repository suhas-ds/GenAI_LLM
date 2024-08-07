# src/text_utils.py
import textwrap

# Function to wrap text while preserving newlines
def wrap_text_preserve_newlines(text, width=110):
    lines = text.split('\n')
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]
    wrapped_text = '\n'.join(wrapped_lines)
    return wrapped_text

def clean_response(ans_):
  ans_ = ans_.split('\n')[0].strip()
  return ans_
import streamlit as st
import nbformat
from nbconvert import PythonExporter
import io

# Load the Jupyter Notebook
notebook_path = 'KaggleTest2.ipynb'  # Replace with the path to your .ipynb file
with io.open(notebook_path, 'r', encoding='utf-8') as notebook_file:
    notebook_content = nbformat.read(notebook_file, as_version=4)

# Convert the notebook to Python code
python_exporter = PythonExporter()
python_code, _ = python_exporter.from_notebook_node(notebook_content)

# Display the Streamlit app
st.code(python_code)

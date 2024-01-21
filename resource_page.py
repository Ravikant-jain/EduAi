import streamlit as st

import PyPDF2

file = st.file_uploader("Upload a PDF file", type="pdf")
if file is not None:
    # Read the PDF file
    pdf_reader = PyPDF2.PdfReader(file)
    # Extract the content
    content = ""
    for page in range(len(pdf_reader.pages)):
        content += pdf_reader.pages[page].extract_text()
    # Display the content
    st.write(content)
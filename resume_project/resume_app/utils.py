import pdfplumber
import docx
import os

def extract_text_from_resume(file_path):
    """
    Extract text from a resume file (PDF or DOCX).
    """
    ext = os.path.splitext(file_path)[1]
    text = ""
    if ext == '.pdf':
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text+=page.extract_text() or ''
    elif ext == '.docx':
        doc = docx.Document(file_path)
        text = '\n'.join([para.text for para in doc.paragraphs])
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or DOCX file.")

    return text

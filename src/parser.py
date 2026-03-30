import pdfplumber
import docx


def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def extract_text_from_docx(docx_file):
    text = ""
    document = docx.Document(docx_file)

    for para in document.paragraphs:
        text += para.text + "\n"

    return text


def extract_resume_text(uploaded_file):
    """
    Detect file type and extract resume text accordingly.
    Supports PDF and DOCX.
    """

    file_name = uploaded_file.name

    if file_name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)

    elif file_name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)

    else:
        return None

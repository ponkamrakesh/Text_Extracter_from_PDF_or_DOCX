from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import pdfplumber
import docx
import os
from jinja2 import Template

app = FastAPI()

# Load HTML Template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Resume Analyzer</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin: 50px; }
        form { margin-bottom: 20px; }
    </style>
</head>
<body>
    <h1>Resume Analyzer</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload Resume</button>
    </form>
    {% if text %}
        <h2>Extracted Resume Content</h2>
        <pre>{{ text }}</pre>
    {% endif %}
</body>
</html>
"""


# Extract text from PDF
def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])


# Extract text from DOCX
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])


@app.get("/", response_class=HTMLResponse)
async def home():
    return Template(html_template).render()


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = f"uploads/{file.filename}"

    # Ensure the uploads folder exists
    os.makedirs("uploads", exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Extract text based on file type
    extracted_text = ""
    if file.filename.endswith(".pdf"):
        extracted_text = extract_text_from_pdf(file_path)
    elif file.filename.endswith(".docx"):
        extracted_text = extract_text_from_docx(file_path)
    else:
        return {"error": "Only PDF and DOCX files are supported"}

    # Return extracted text in HTML format
    return Template(html_template).render(text=extracted_text)

# Resume Analyzer - FastAPI Web Application

This is a simple **FastAPI web application** that allows users to upload resumes (PDF or DOCX), extracts the text, and displays it on the webpage.

## Features
- Upload **PDF** or **DOCX** resumes.
- Extract text using **pdfplumber** (for PDFs) and **python-docx** (for DOCX).
- Display extracted text in a web-based UI.
- Built using **FastAPI** and **Jinja2** templating.

---

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/resume-analyzer.git
   cd resume-analyzer
Install dependencies

bash

pip install fastapi uvicorn python-multipart pdfplumber python-docx jinja2
Run the FastAPI server

uvicorn main:app --reload

Open in Browser

http://127.0.0.1:8000/

📂 Project Structure

resume-analyzer/
│── main.py              # FastAPI backend
│── README.md            # Project documentation
│── uploads/             # Stores uploaded resumes (auto-created)

🛠️ How It Works
Open the web app at http://127.0.0.1:8000/
Upload a PDF or DOCX resume.
The app extracts text and displays it on the screen.
⚡ API Endpoints
Endpoint	Method	Description
/	GET	Home page (HTML form)
/upload	POST	Uploads and extracts text from resume




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
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi uvicorn python-multipart pdfplumber python-docx jinja2
   ```

3. **Run the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```

4. **Open in Browser**
   ```
   http://127.0.0.1:8000/
   ```

---

## 📂 Project Structure
```
resume-analyzer/
│── main.py              # FastAPI backend
│── README.md            # Project documentation
│── uploads/             # Stores uploaded resumes (auto-created)
```

---

## 🛠️ How It Works

1. Open the web app at **http://127.0.0.1:8000/**
2. Upload a **PDF** or **DOCX** resume.
3. The app extracts text and displays it on the screen.

---

## ⚡ API Endpoints

| Endpoint  | Method | Description |
|-----------|--------|-------------|
| `/`       | GET    | Home page (HTML form) |
| `/upload` | POST   | Uploads and extracts text from resume |

---

## 💡 Future Enhancements
- **AI-based Job Matching** using NLP.
- **Database Storage** for resumes.
- **Enhanced UI** with Bootstrap/React.

---

## 📜 License
This project is licensed under the **MIT License**.


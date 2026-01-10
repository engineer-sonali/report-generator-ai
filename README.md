# AI Report Generator

AI Report Generator is a FastAPI-based backend application that generates structured **business analytics reports in PDF format** using uploaded CSV files and images. The system combines traditional data analytics with AI-powered insights and vector-based semantic search.

---

## 🚀 Tech Stack

### Backend
- **FastAPI** – High-performance Python web framework
- **Uvicorn** – ASGI server for FastAPI
- **Pydantic** – Data validation and request/response schemas

### Data Storage
- **PostgreSQL (Local)** – Persistent storage for:
  - Uploaded file metadata
  - Report generation history
  - Structured analytics results
- **SQLAlchemy** – ORM for database interaction

### Vector Database
- **Qdrant** – Vector database for:
  - Storing text embeddings
  - Semantic search over reports and CSV content
  - Similarity-based retrieval during report generation

### Data Processing
- **Pandas** – CSV parsing, cleaning, and analytics
- **NumPy** – Numerical computations
- **Python-Multipart** – File upload handling

### AI / NLP
- **LangChain** – LLM workflow orchestration
- **OpenAI API** – Natural language report generation
- **Sentence-Transformers** – Text embedding generation
- **Torch (CPU)** – Backend for embedding models

### Document Generation
- **PDF generation utilities (ReportLab or equivalent)** – PDF creation
- **Pillow (PIL)** – Image preprocessing and embedding

### Configuration & DevOps
- **python-dotenv** – Environment variable management
- **GitHub** – Version control
- **Render (attempted)** – Cloud deployment platform

---

## 🧠 Architecture Overview

- **PostgreSQL** is used for structured, relational data:
  - File references
  - Report metadata
  - Processing status
- **Qdrant** stores high-dimensional embeddings generated from:
  - CSV textual content
  - AI-generated summaries
  - Image-derived text (if applicable)
- **LangChain** retrieves relevant vectors from Qdrant to enrich report generation with contextual data.

---

## 📄 Types of Reports Generated (PDF)

### 1️⃣ Business Analytics Reports
- CSV-based statistical summaries
- Aggregated metrics and trends
- AI-generated interpretations

### 2️⃣ Semantic Insight Reports
- Context-aware summaries powered by vector search
- Similarity-based insights retrieved from Qdrant embeddings

### 3️⃣ Image + Data Reports
- Embedded charts and images
- AI explanations linked to stored embeddings

### 4️⃣ Automated Executive Reports
- Natural-language summaries
- Actionable recommendations

---

## 📂 Supported Input Formats
- **CSV files**
- **Image files (PNG, JPG)**

---

## 📤 Output Format
- **PDF (.pdf)** – Shareable, presentation-ready reports

## Swagger UI


## PDF Generated
📄 [Download Sample Analytics Report (PDF)](app/storage/reports/report(10).pdf)



# 🚀 InsightForgeAI

## Enterprise AI Document Intelligence Platform

Upload • Process • Search • Chat with Enterprise Documents using AI

Built with Python, FastAPI, React, Retrieval-Augmented Generation (RAG), Vector Search, and Large Language Models.

---

## 📖 Overview

InsightForgeAI is an AI-powered document intelligence platform that enables users to upload PDF documents, extract and process their content, perform intelligent document retrieval, and interact with enterprise knowledge using modern AI techniques.

The project follows a modular architecture and is designed to simulate a production-grade enterprise AI application.

---

## ✨ Current Features

- ✅ PDF Upload API
- ✅ Document Processing Pipeline
- ✅ Text Extraction
- ✅ Intelligent Document Chunking
- ✅ Metadata Generation
- ✅ Processed Documents API
- ✅ Keyword-based Document Search
- ✅ REST APIs using FastAPI
- ✅ Interactive Swagger Documentation

---

## 🚧 Features In Progress

- Embedding Generation
- Vector Database Integration
- Semantic Search
- Retrieval-Augmented Generation (RAG)
- AI Chat Assistant
- Authentication
- Docker Deployment

---

## 🛠️ Tech Stack

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic

### Frontend

- React
- JavaScript
- HTML
- CSS

### AI

- Retrieval-Augmented Generation (RAG)
- Vector Search
- Large Language Models (In Progress)

### Tools

- Git
- GitHub
- VS Code

---

## 🏗️ Architecture

```
                 React Frontend
                        │
                        ▼
                 FastAPI Backend
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
   PDF Processing                Search APIs
        │                               │
        ▼                               ▼
 Intelligent Chunking          Keyword Retrieval
        │
        ▼
 Embeddings (In Progress)
        │
        ▼
 Vector Search (In Progress)
        │
        ▼
      RAG Chat
```

---

## 📂 Project Structure

```
InsightForgeAI
│
├── backend
│   ├── app
│   ├── uploads
│   ├── processed
│   └── requirements.txt
│
├── docs
│
└── README.md
```

---

## 🚀 Running the Project

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend:

```
http://localhost:8000
```

Swagger:

```
http://localhost:8000/docs
```

---

## 📅 Roadmap

- ✅ FastAPI Backend
- ✅ PDF Upload
- ✅ Document Processing
- ✅ Keyword Search
- 🚧 Embedding Generation
- 🚧 Vector Search
- 🚧 Semantic Search
- 🚧 RAG
- 🚧 AI Chat
- 🚧 Authentication

---

## 🎯 Purpose

This project demonstrates enterprise-level AI application development using Python, FastAPI, modern REST APIs, document processing, and Retrieval-Augmented Generation (RAG) concepts.

---

## 👨‍💻 Author

**Dharani**

GitHub: https://github.com/dt0806

# Software Requirements Specification (SRS)

# Project Name

InsightForgeAI

---

# 1. Introduction

## Purpose

InsightForgeAI is an AI-powered document intelligence platform that enables users to upload PDF documents, perform semantic search, and ask natural language questions using Retrieval-Augmented Generation (RAG).

The project demonstrates production-style backend software engineering using modern AI technologies.

---

# 2. Project Objectives

The system shall allow users to:

- Upload PDF documents.
- Extract text from uploaded PDFs.
- Split documents into manageable chunks.
- Generate semantic embeddings.
- Perform semantic document search.
- Generate grounded AI answers using OpenAI.
- Return source citations with every answer.

---

# 3. Functional Requirements

## FR-1 Document Upload

The system shall allow users to upload PDF documents through a REST API.

---

## FR-2 Text Extraction

The system shall extract text from uploaded PDF documents.

---

## FR-3 Text Chunking

The system shall split extracted text into overlapping chunks for retrieval.

---

## FR-4 Embedding Generation

The system shall generate vector embeddings for each document chunk using Sentence Transformers.

---

## FR-5 Metadata Storage

The system shall store:

- document metadata
- chunk metadata
- embedding vectors

for later retrieval.

---

## FR-6 Semantic Search

The system shall retrieve the most relevant document chunks using vector similarity.

---

## FR-7 Retrieval-Augmented Generation

The system shall:

- retrieve relevant chunks
- build context
- send context to OpenAI
- generate grounded answers

---

## FR-8 Source References

Every generated answer shall include the document chunks used to generate the response.

---

## FR-9 API Documentation

The system shall expose interactive API documentation using Swagger.

---

## FR-10 Automated Testing

The system shall include automated unit and integration tests.

---

## FR-11 Continuous Integration

The system shall automatically execute the test suite using GitHub Actions on every push.

---

# 4. Non-Functional Requirements

The application shall provide:

- Modular architecture
- Maintainable code
- Testable services
- RESTful APIs
- Clear separation of concerns
- Consistent error handling

---

# 5. Technology Stack

Backend

- Python
- FastAPI
- Uvicorn
- Pydantic

AI

- Sentence Transformers
- OpenAI API

Testing

- Pytest

CI/CD

- GitHub Actions

Development

- Git
- GitHub
- VS Code

---

# 6. Future Enhancements

Future versions may include:

- React frontend
- Docker deployment
- PostgreSQL
- Vector database integration
- Authentication
- Multi-document search
- Cloud deployment
- Role-based access control

---

# 7. Success Criteria

The project is considered successful when it can:

- Upload PDF documents successfully.
- Extract document text.
- Generate semantic embeddings.
- Perform semantic search.
- Produce grounded RAG responses.
- Return source citations.
- Pass the automated test suite.
- Successfully execute GitHub Actions CI.
# InsightForgeAI Architecture

## Overview

InsightForgeAI follows a modern enterprise architecture consisting of a React frontend, FastAPI backend, AI services, and data engineering pipelines.

The frontend provides an intuitive interface for uploading documents, datasets, and interacting with AI.

The backend orchestrates requests between document processing, AI services, data analysis, databases, and external AI models.

The platform separates responsibilities into dedicated services to improve scalability, maintainability, and performance.

---

## High-Level Components

- React Frontend
- FastAPI Backend
- Document Service
- Data Service
- AI Service
- PostgreSQL
- Qdrant Vector Database
- OpenAI / Azure OpenAI
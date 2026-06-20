# Enterprise RAG ChatBot

A full-stack AI-powered ChatBot platform built with React, FastAPI, PostgreSQL, and OpenAI.

The platform supports conversational AI, document uploads, Retrieval-Augmented Generation (RAG), semantic search, user authentication, conversation management, and administration features.

---

# Architecture Overview

```text
┌─────────────────────┐
│     React Frontend  │
│     (Vite + React)  │
└──────────┬──────────┘
           │ REST API
           ▼
┌─────────────────────┐
│    FastAPI Backend  │
│ Authentication      │
│ Chat Services       │
│ File Services       │
│ RAG Services        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│     PostgreSQL      │
│ Users              │
│ Conversations      │
│ Messages           │
│ Documents          │
│ Embeddings         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      OpenAI API     │
│ GPT Models          │
│ Embeddings          │
└─────────────────────┘
```

---

# Features

## Authentication

* User Registration
* User Login
* JWT Authentication
* Role-Based Access Control
* Protected API Endpoints

---

## Conversational AI

* ChatGPT-style Interface
* Streaming AI Responses
* Conversation History
* Multi-Conversation Support
* Persistent Messages

---

## Retrieval-Augmented Generation (RAG)

* PDF Upload
* TXT Upload
* Markdown Upload
* Text Extraction
* Document Chunking
* OpenAI Embeddings
* Semantic Search
* Context-Aware Responses

---

## Administration

* User Statistics
* Usage Tracking
* Conversation Analytics
* Admin Dashboard APIs

---

## Production Features

* FastAPI
* PostgreSQL
* SQLAlchemy ORM
* Alembic Migrations
* OpenAI Integration
* Rate Limiting
* Automated Testing
* Modular Service Architecture

---

# Technology Stack

## Frontend

| Technology | Purpose           |
| ---------- | ----------------- |
| React      | UI Framework      |
| Vite       | Build Tool        |
| JavaScript | Frontend Logic    |
| Fetch API  | API Communication |

---

## Backend

| Technology | Purpose             |
| ---------- | ------------------- |
| FastAPI    | API Framework       |
| PostgreSQL | Database            |
| SQLAlchemy | ORM                 |
| Alembic    | Database Migrations |
| OpenAI     | LLM & Embeddings    |
| JWT        | Authentication      |
| SlowAPI    | Rate Limiting       |
| PyPDF      | PDF Processing      |
| Pytest     | Testing             |

---

# Project Structure

```text
project-root/
│
├── backend/
│   │
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── alembic/
│   ├── tests/
│   ├── uploads/
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   │
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   ├── config.js
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── public/
│   ├── package.json
│   └── .env
│
└── README.md
```

---

# Getting Started

## Clone Repository

```bash
git clone https://github.com/yourusername/enterprise-rag-chatbot.git

cd enterprise-rag-chatbot
```

---

# Backend Setup

## Create Virtual Environment

```bash
cd backend

python -m venv venv

source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create:

```text
backend/.env
```

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/chatbot_db

OPENAI_API_KEY=your_openai_api_key

SECRET_KEY=change-this-secret

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## Create Database

```sql
CREATE DATABASE chatbot_db;
```

---

## Run Migrations

```bash
alembic upgrade head
```

---

## Start Backend

```bash
uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

## Install Dependencies

```bash
cd frontend

npm install
```

---

## Configure Environment

Create:

```text
frontend/.env
```

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

---

## Start Frontend

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# API Endpoints

## Authentication

| Method | Endpoint       |
| ------ | -------------- |
| POST   | /auth/register |
| POST   | /auth/login    |
| GET    | /auth/me       |

---

## Chat

| Method | Endpoint     |
| ------ | ------------ |
| POST   | /chat/stream |

---

## Files

| Method | Endpoint      |
| ------ | ------------- |
| POST   | /files/upload |

---

## Conversations

| Method | Endpoint                     |
| ------ | ---------------------------- |
| GET    | /conversations               |
| GET    | /conversations/{id}/messages |
| DELETE | /conversations/{id}          |

---

## Admin

| Method | Endpoint     |
| ------ | ------------ |
| GET    | /admin/stats |
| GET    | /admin/users |
| GET    | /admin/usage |

---

# Testing

Run backend tests:

```bash
cd backend

python -m pytest
```

Run coverage:

```bash
pytest --cov=app
```

---

# RAG Workflow

```text
Upload Document
        │
        ▼
Extract Text
        │
        ▼
Chunk Document
        │
        ▼
Generate Embeddings
        │
        ▼
Store in PostgreSQL
        │
        ▼
Semantic Search
        │
        ▼
Retrieve Relevant Chunks
        │
        ▼
Generate AI Response
```

---

# Future Roadmap

* pgvector Integration
* Multi-Model Routing
* AI Agent Workflows
* Citation-Based Responses
* Source Attribution
* Conversation Summarization
* Docker Deployment
* Kubernetes Deployment
* CI/CD Pipelines
* Observability & Monitoring
* Multi-Tenant Architecture

---

# Security Notes

Never commit:

```text
.env
uploads/
venv/
node_modules/
```

Use:

```text
.env.example
```

for sharing configuration templates.

---

# License

MIT License

---

# Author

Jay Ram Singh

Founder, Altmatic Technologies LLP

Website: https://altmatic.com
LinkedIn: https://www.linkedin.com/in/jayram

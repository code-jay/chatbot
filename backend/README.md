# Enterprise RAG ChatBot Backend

A production-oriented AI ChatBot backend built with FastAPI, PostgreSQL, OpenAI, and Retrieval-Augmented Generation (RAG).

## Features

### Authentication & Authorization

* User Registration
* User Login
* JWT Authentication
* Role-Based Access Control (Admin/User)

### Conversational AI

* Streaming AI Responses
* Multi-Conversation Support
* Conversation History
* Message Persistence

### Retrieval-Augmented Generation (RAG)

* PDF Upload Support
* TXT Upload Support
* Markdown Upload Support
* Document Chunking
* OpenAI Embeddings
* Semantic Search
* Context-Aware Responses

### Administration

* User Statistics
* Usage Statistics
* Conversation Analytics
* System Monitoring

### Production Features

* PostgreSQL Database
* SQLAlchemy ORM
* Alembic Database Migrations
* Rate Limiting
* Environment-Based Configuration
* Automated Testing
* Modular Service Architecture

---

# Technology Stack

| Component       | Technology             |
| --------------- | ---------------------- |
| API Framework   | FastAPI                |
| Database        | PostgreSQL             |
| ORM             | SQLAlchemy             |
| Migrations      | Alembic                |
| Authentication  | JWT                    |
| AI Models       | OpenAI                 |
| Embeddings      | text-embedding-3-small |
| Testing         | Pytest                 |
| File Processing | PyPDF                  |
| Rate Limiting   | SlowAPI                |

---

# Project Structure

```text
app/
│
├── api/
│   └── v1/
│       ├── auth.py
│       ├── chat.py
│       ├── files.py
│       ├── admin.py
│       └── conversations.py
│
├── core/
│   ├── config.py
│   ├── security.py
│   ├── dependencies.py
│   ├── middleware.py
│   └── rate_limit.py
│
├── db/
│   ├── database.py
│   ├── session.py
│   └── init_db.py
│
├── models/
│
├── schemas/
│
├── services/
│   ├── ai_gateway/
│   ├── auth/
│   ├── chat/
│   ├── files/
│   ├── rag/
│   └── utils/
│
└── main.py

tests/
alembic/
uploads/
```

---

# Setup

## Clone Repository

```bash
git clone https://github.com/yourusername/chatbot-backend.git

cd chatbot-backend
```

## Create Virtual Environment

```bash
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

# Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/chatbot_db

OPENAI_API_KEY=your_openai_api_key

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

# Database Setup

Create PostgreSQL database:

```sql
CREATE DATABASE chatbot_db;
```

Run migrations:

```bash
alembic upgrade head
```

---

# Start Server

```bash
uvicorn app.main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
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
| DELETE | /conversations/{id}          |
| GET    | /conversations/{id}/messages |

---

## Admin

| Method | Endpoint     |
| ------ | ------------ |
| GET    | /admin/stats |
| GET    | /admin/users |
| GET    | /admin/usage |

---

# Running Tests

Run all tests:

```bash
python -m pytest
```

Run with coverage:

```bash
pytest --cov=app
```

---

# RAG Workflow

```text
User Uploads Document
        │
        ▼
Text Extraction
        │
        ▼
Chunking
        │
        ▼
OpenAI Embeddings
        │
        ▼
Store in PostgreSQL
        │
        ▼
Semantic Search
        │
        ▼
Relevant Context
        │
        ▼
LLM Response Generation
```

---

# Future Improvements

* Vector Database Integration (pgvector)
* Multi-Model Routing
* Agentic Workflows
* Citation-Based Responses
* Conversation Summaries
* Evaluation Framework
* Docker Deployment
* CI/CD Pipeline
* Kubernetes Deployment
* Observability & Monitoring

---

# License

MIT License

---

# Author

Jay Ram Singh

Founder, Altmatic Technologies LLP

https://altmatic.com

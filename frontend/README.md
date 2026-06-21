# Enterprise RAG ChatBot Frontend

A modern ChatGPT-style frontend built with React, Vite, and FastAPI integration.

This application provides a conversational interface for interacting with AI models, uploading documents, and querying information using Retrieval-Augmented Generation (RAG).

---

# Features

### Authentication

* User Registration
* User Login
* JWT Token Management
* Persistent Login Sessions

### Chat Experience

* Real-Time Streaming Responses
* ChatGPT-Style Interface
* Conversation History
* Multiple Conversations
* Auto Conversation Creation

### File Upload & RAG

* PDF Upload
* TXT Upload
* Markdown Upload
* Document Summarization
* Context-Aware Question Answering

### User Experience

* Responsive Design
* Sidebar Conversation Management
* Loading Indicators
* Error Handling
* Authentication-Aware Navigation

---

# Technology Stack

| Component          | Technology |
| ------------------ | ---------- |
| Frontend Framework | React      |
| Build Tool         | Vite       |
| Language           | JavaScript |
| Styling            | CSS        |
| API Communication  | Fetch API  |
| Authentication     | JWT        |
| Backend            | FastAPI    |

---

# Project Structure

```text
src/
│
├── components/
│   ├── Login.jsx
│   ├── Register.jsx
│   ├── ChatWindow.jsx
│   ├── Message.jsx
│   ├── Sidebar.jsx
│   └── FileUpload.jsx
│
├── services/
│   └── api.js
│
├── config.js
│
├── App.jsx
│
├── main.jsx
│
└── index.css

public/

vite.config.js
package.json
```

---

# Setup

## Clone Repository

```bash
git clone https://github.com/yourusername/chatbot-frontend.git

cd chatbot-frontend
```

---

## Install Dependencies

```bash
npm install
```

or

```bash
yarn install
```

---

# Environment Variables

Create a `.env` file in the project root.

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

Production Example:

```env
VITE_API_BASE_URL=https://api.yourdomain.com
```

---

# Start Development Server

```bash
npm run dev
```

Application:

```text
http://localhost:5173
```

---

# Build for Production

```bash
npm run build
```

Generated files:

```text
dist/
```

---

# API Integration

The frontend communicates with the backend through a centralized API configuration.

## config.js

```javascript
export const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL ||
  "http://127.0.0.1:8000";
```

## Example Usage

```javascript
const response = await fetch(
  `${API_BASE_URL}/auth/login`,
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
      password,
    }),
  }
);
```

---

# Features Overview

## Authentication Flow

```text
User Login
     │
     ▼
JWT Token Received
     │
     ▼
Stored in Local Storage
     │
     ▼
Used for API Requests
```

---

## Chat Flow

```text
User Message
      │
      ▼
FastAPI Backend
      │
      ▼
OpenAI / RAG Processing
      │
      ▼
Streaming Response
      │
      ▼
Live UI Updates
```

---

## Document Upload Flow

```text
Upload Document
       │
       ▼
Backend Processing
       │
       ▼
Text Extraction
       │
       ▼
Chunking & Embeddings
       │
       ▼
Stored in Database
       │
       ▼
Available for Chat Queries
```

---

# Scripts

## Development

```bash
npm run dev
```

## Production Build

```bash
npm run build
```

## Preview Build

```bash
npm run preview
```

---

# Future Improvements

* Dark Mode
* User Profile Management
* Chat Export
* Drag & Drop Upload
* Markdown Rendering
* Code Syntax Highlighting
* Chat Search
* Multi-File Support
* Source Citations
* Mobile Optimization
* Voice Input
* Speech-to-Text

---

# Backend Repository

The frontend requires the FastAPI backend to be running.

Backend URL:

```text
http://127.0.0.1:8000
```

Update through:

```env
VITE_API_BASE_URL
```

---

# License

MIT License

---

# Author

Jay Ram Singh

LinkedIn: https://www.linkedin.com/in/jayram
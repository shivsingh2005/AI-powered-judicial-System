<div align="center">
  
  
  # AI-Powered Legal Justice Hub
  
  <p>
    An AI-driven legal assistance platform that uses Large Language Models (LLMs) to provide comprehensive legal analysis for Indian citizens, advocates, and judges.
  </p>
  
  <p>
    <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python">
    <img src="https://img.shields.io/badge/TypeScript-5.0+-3178C6.svg" alt="TypeScript">
    <img src="https://img.shields.io/badge/FastAPI-0.100+-009688.svg" alt="FastAPI">
    <img src="https://img.shields.io/badge/React-18+-61DAFB.svg" alt="React">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  </p>
</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **LLM-Powered Content** | All legal analysis, case research, and document generation uses Groq LLMs |
| 📋 **Comprehensive Legal Analysis** | Dispute analysis, similar case finding, legal arguments generation |
| 🔍 **Research & Insights** | AI-powered legal research with RAG search capabilities |
| ⚖️ **Bias Detection** | Automatic analysis of legal documents for bias and fairness |
| 👥 **Multi-Role Support** | Citizen, Advocate, and Judge interfaces with specialized features |

---

## 📋 Prerequisites

- **Node.js** (v16 or higher)
- **Python** 3.9+ (for backend)
- **Groq API Key** — Get one at [https://console.groq.com/](https://console.groq.com/)

---

## 🚀 Quick Setup

### 1. Clone & Install Dependencies

```
bash
# Frontend
npm install

# Backend
cd app
pip install -r requirements.txt
```

### 2. Environment Configuration

Create a `.env.local` or `.env` file in the root directory:

```
env
GROQ_API_KEY=your_groq_api_key_here
VITE_API_URL=http://localhost:8001/api
```

---

## 🏃 Running Locally

| Service | Command | URL |
|---------|---------|-----|
| **Backend** | `python main.py` | `http://localhost:8001/api` |
| **Frontend** | `npm run dev` | `http://localhost:5173` |

---

## ⚠️ Important Notes

> **No Mock Data**: This application uses only LLM-generated content. If you don't provide a valid `GROQ_API_KEY`, the application will fail gracefully with clear error messages.

### Requirements for Full Functionality
- ✅ Valid Groq API Key
- ✅ Internet connection to reach Groq API
- ✅ Sufficient API credits

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | React, TypeScript, Vite |
| **Backend** | FastAPI, Python |
| **AI/ML** | Groq LLM, LangChain |
| **Styling** | CSS3, Modern UI Components |

---

## 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">
  <p>Built with ❤️ using AI and Legal Technology</p>
</div>

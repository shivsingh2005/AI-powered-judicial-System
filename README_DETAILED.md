# AI Justice Hub: AI-Driven Judicial Precedent & Case Management Ecosystem

<div align="center">

![AI Justice Hub](https://img.shields.io/badge/AI%20Justice%20Hub-Legal%20Tech-blue?style=for-the-badge)
![React](https://img.shields.io/badge/React-19.2-61DAFB?style=flat&logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688?style=flat&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python)
![TypeScript](https://img.shields.io/badge/TypeScript-5.8-3178C6?style=flat&logo=typescript)
![License](https://img.shields.io/badge/License-MIT-green)

*An advanced, AI-powered legal management platform enabling citizens, advocates, and judges to navigate the Indian judicial system with intelligent case analysis, precedent research, and legal document generation.*

---

</div>

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Project Architecture](#project-architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Component Guide](#component-guide)
- [Features by User Role](#features-by-user-role)
- [AI & LLM Integration](#ai--llm-integration)
- [Data Privacy & Compliance](#data-privacy--compliance)
- [Development Guidelines](#development-guidelines)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## 🎯 Overview

**AI Justice Hub** is a comprehensive legal technology platform designed to democratize access to justice in India. It leverages artificial intelligence, large language models, and intelligent case analysis to empower three distinct user roles:

- **Citizens**: File cases, understand legal summaries, and receive lawyer recommendations
- **Advocates**: Research precedents, build legal arguments, and analyze case analytics
- **Judges**: Access case analysis, detect bias, review explainable AI insights, and maintain immutable case logs

The platform is built with a modern **React + TypeScript** frontend and a **FastAPI + Langchain + Groq** backend, emphasizing scalability, privacy compliance, and user-centric AI-driven legal insights.

### Mission
To bridge the gap between citizens and the judicial system by providing accessible, AI-powered legal intelligence that accelerates case resolution and promotes fair, transparent, and efficient justice delivery.

---

## ✨ Key Features

### Citizen Features
- **Case Filing & Analysis**: File cases with detailed dispute descriptions
- **AI-Powered Case Classification**: Automatic categorization of legal issues
- **Lawyer Recommendations**: Intelligent suggestions based on case analysis
- **Legal Summaries**: Comprehensive AI-generated summaries of legal disputes
- **Probable Remedies**: AI-suggested legal remedies and outcomes
- **Case Chat Interface**: Real-time discussion with AI legal assistant
- **Multi-Language Support**: Support for 7 Indian languages (English, Hindi, Bengali, Marathi, Tamil, Telugu, Kannada)

### Advocate Features
- **Precedent Search Engine**: Full-text search across judicial precedents
- **Argument Builder**: AI-assisted legal argument construction
- **Case Analytics**: Data-driven insights on case outcomes and trends
- **Judicial Analytics Dashboard**: Comprehensive case statistics and patterns
- **Legal Research Hub**: Access to AI-powered legal research tools
- **Similar Case Analyzer**: Find and analyze similar legal cases
- **Performance Metrics**: Track case success rates and outcomes

### Judge Features
- **Judicial Dashboard**: Comprehensive case management interface
- **Explainable AI Insights**: Transparent AI reasoning for case analysis
- **Bias Detection**: Identify potential biases in case arguments
- **Blockchain Case Logs**: Immutable, transparent case record management
- **Influencing Statutes**: Relevant legal statutes and their application
- **Consistency Checks**: Validate consistency across case arguments
- **Analytics Dashboard**: Judicial performance metrics and insights

### Cross-Role Features
- **Theme Support**: Light/Dark mode for improved accessibility
- **Multi-Language Interface**: 7 Indian languages with complete translations
- **Real-Time Chat**: AI-powered conversational interface
- **Legal Document Generation**: Automated generation of legal drafts
- **Responsive Design**: Optimized for desktop and tablet devices
- **DPDP Act 2023 Compliance**: Privacy-first data handling

---

## 🏗️ Project Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    FRONTEND (React + TypeScript)             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Components Layer                                    │   │
│  │  - User Dashboards (Citizen, Advocate, Judge)       │   │
│  │  - Chat Interface, Case Filing, Search              │   │
│  │  - Analytics & Visualizations                       │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Services Layer                                      │   │
│  │  - Gemini Service (LLM Integration)                 │   │
│  │  - API Communication                                │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                          ↓ HTTPS/REST ↓
┌─────────────────────────────────────────────────────────────┐
│                 BACKEND (FastAPI + Python)                   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  API Routes Layer                                    │   │
│  │  - /api/citizen      - Citizen operations           │   │
│  │  - /api/advocate     - Advocate operations          │   │
│  │  - /api/judge        - Judge operations             │   │
│  │  - /api/chat         - Chat operations              │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Services Layer (AI)                                 │   │
│  │  - AI Service (Langchain + Groq LLM)                │   │
│  │  - Case Analysis Engine                             │   │
│  │  - Precedent Analysis                               │   │
│  │  - Legal Document Generation                        │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Data Models (Pydantic)                              │   │
│  │  - CitizenAnalysisResult                            │   │
│  │  - RecommendedLawyer                                │   │
│  │  - CaseAnalysis                                     │   │
│  │  - ChatMessage                                      │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│           EXTERNAL SERVICES & DATA SOURCES                   │
│  - Groq LLM API (Langchain Integration)                      │
│  - Precedent Database                                        │
│  - Judicial Records                                          │
│  - Legal Statutes & Regulations                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 💻 Tech Stack

### Frontend
| Technology | Version | Purpose |
|-----------|---------|---------|
| **React** | 19.2.0 | UI Framework |
| **TypeScript** | 5.8.2 | Type-Safe JavaScript |
| **Vite** | 6.2.0 | Build Tool & Dev Server |
| **Chart.js** | 4.5.1 | Data Visualization |
| **Tailwind CSS** | (Built-in) | Styling |
| **Google Genai** | 1.28.0 | LLM Integration |

### Backend
| Technology | Version | Purpose |
|-----------|---------|---------|
| **FastAPI** | 0.109.0+ | Web Framework |
| **Uvicorn** | 0.27.0+ | ASGI Server |
| **Python** | 3.8+ | Language |
| **Langchain** | 0.3.0+ | LLM Framework |
| **Langchain-Groq** | 0.1.10+ | Groq Integration |
| **Pydantic** | 2.10.0+ | Data Validation |
| **Python-dotenv** | 1.0.0+ | Environment Management |

### External Services
- **Groq LLM API**: LLM inference (llama-3.1-8b-instant)
- **Google Gemini API**: Secondary LLM option

---

## 📁 Project Structure

```
gla/
├── Frontend (React + TypeScript)
│   ├── App.tsx                          # Main application component
│   ├── main.tsx                         # Entry point
│   ├── index.tsx                        # React DOM render
│   ├── index.html                       # HTML template
│   ├── vite.config.ts                   # Vite configuration
│   ├── tsconfig.json                    # TypeScript configuration
│   ├── types.ts                         # Shared TypeScript types
│   ├── featureFlags.ts                  # Feature flag management
│   │
│   ├── components/                      # React Components
│   │   ├── DashboardLayout.tsx          # Main layout wrapper
│   │   ├── LoginPage.tsx                # Authentication
│   │   │
│   │   ├── CitizenDashboard.tsx         # Citizen home
│   │   ├── AdvocateDashboard.tsx        # Advocate home
│   │   ├── JudgeDashboard.tsx           # Judge home
│   │   │
│   │   ├── CaseFiling.tsx               # Case submission form
│   │   ├── DisputeInputForm.tsx         # Dispute details
│   │   ├── CaseChat.tsx                 # Case discussion chat
│   │   ├── ResultsDisplay.tsx           # Analysis results
│   │   │
│   │   ├── PrecedentSearch.tsx          # Precedent search UI
│   │   ├── ArgumentBuilder.tsx          # Argument construction
│   │   ├── AnalyticsDashboard.tsx       # Analytics dashboard
│   │   │
│   │   ├── ExplainableAI.tsx            # AI explainability
│   │   ├── SimilarCaseAnalyzer.tsx      # Case similarity analysis
│   │   ├── BlockchainLog.tsx            # Case log blockchain
│   │   │
│   │   ├── Chatbot.tsx                  # General purpose chatbot
│   │   ├── AIResearchHub.tsx            # AI research tools
│   │   ├── Workspace.tsx                # Workspace management
│   │   │
│   │   ├── addons/                      # Optional add-on components
│   │   │   ├── BiasMonitor.tsx          # Bias detection UI
│   │   │   ├── LegalDraftGenerator.tsx  # Document generation
│   │   │   ├── Notifications.tsx        # Notification system
│   │   │   └── SmartCalendar.tsx        # Case calendar
│   │   │
│   │   ├── icons/                       # Icon components (SVG)
│   │   │   ├── GavelIcon.tsx
│   │   │   ├── BellIcon.tsx
│   │   │   └── [20+ icon components]
│   │   │
│   │   └── [Navigation & Utility Components]
│   │       ├── Header.tsx
│   │       ├── Sidebar.tsx
│   │       ├── LanguageSelector.tsx
│   │       └── Spinner.tsx
│   │
│   ├── services/
│   │   └── geminiService.ts             # Frontend LLM service
│   │
│   ├── contexts/
│   │   └── LanguageContext.tsx          # Language state management
│   │
│   ├── hooks/
│   │   └── useTranslations.ts           # Translation hook
│   │
│   ├── data/
│   │   └── mockData.ts                  # Mock/seed data
│   │
│   ├── translations/
│   │   └── strings.ts                   # Multi-language strings
│   │
│   ├── index.css                        # Global styles
│   ├── package.json                     # Frontend dependencies
│   └── README.md                        # Original README

├── Backend (FastAPI + Python)
│   ├── main.py                          # FastAPI application entry point
│   ├── requirements.txt                 # Python dependencies
│   │
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models.py                    # Pydantic data models
│   │   │
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── ai_service.py            # AI service (Groq/Langchain)
│   │   │
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── citizen.py               # Citizen API routes
│   │       ├── advocate.py              # Advocate API routes
│   │       ├── judge.py                 # Judge API routes
│   │       └── chat.py                  # Chat API routes
│   │
│   └── __pycache__/                     # Python cache (ignore)

└── Configuration Files
    ├── .env.local                       # Local environment variables
    ├── .env                             # Environment template
    └── .gitignore                       # Git ignore rules
```

---

## 📋 Prerequisites

Before installing and running the application, ensure you have:

### System Requirements
- **OS**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: 2GB free space
- **Internet Connection**: Required for AI API calls

### Required Software
- **Node.js**: v18.0.0 or higher ([Download](https://nodejs.org/))
  - Includes npm (Node Package Manager) automatically
- **Python**: v3.8 or higher ([Download](https://www.python.org/))
  - Should be added to PATH
- **Git**: For version control ([Download](https://git-scm.com/))

### API Keys Required
1. **Groq API Key**: For LLM inference
   - Get it from: [console.groq.com](https://console.groq.com)
2. **Google Gemini API Key** (Optional): For supplementary AI features
   - Get it from: [ai.google.dev](https://ai.google.dev)

### Verify Installation
```bash
# Check Node.js and npm
node --version
npm --version

# Check Python
python --version

# Check Git
git --version
```

---

## 🚀 Installation

### Step 1: Clone or Download the Repository

```bash
# If using git
git clone <repository-url>
cd gla

# Or if downloaded as ZIP, extract and navigate
cd gla
```

### Step 2: Install Frontend Dependencies

```bash
# Install Node.js dependencies
npm install

# Verify installation
npm list
```

### Step 3: Install Backend Dependencies

```bash
# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Python packages
pip install -r requirements.txt

# Verify installation
pip list
```

### Step 4: Verify Both Installations

```bash
# Frontend verification
npm --version         # Should be v8.0+
npx vite --version   # Should be v6.2.0+

# Backend verification
python --version      # Should be 3.8+
pip list             # Check all packages are installed
```

---

## ⚙️ Configuration

### Frontend Configuration

#### 1. Create `.env.local` file (optional but recommended)

```bash
# In the project root directory
touch .env.local  # macOS/Linux
# or
echo. > .env.local  # Windows
```

#### 2. Add environment variables

```env
# Google Gemini API (if using Gemini backend)
VITE_GEMINI_API_KEY=your_gemini_api_key_here

# API Base URL
VITE_API_URL=http://localhost:8001/api

# Feature flags
VITE_ENABLE_BLOCKCHAIN_LOG=true
VITE_ENABLE_BIAS_DETECTION=true
VITE_ENABLE_DRAFT_GENERATOR=true
```

### Backend Configuration

#### 1. Create `.env.local` file in project root

```bash
# Create the file
touch .env.local  # macOS/Linux
```

#### 2. Add environment variables

```env
# Groq API Configuration (Required)
GROQ_API_KEY=your_groq_api_key_here

# Optional: Google Gemini API
GOOGLE_API_KEY=your_gemini_api_key_here

# Server Configuration
BACKEND_URL=http://localhost:8001
FRONTEND_URL=http://localhost:5173

# CORS Configuration
CORS_ORIGINS=["http://localhost:5173", "http://localhost:3000"]

# Logging
LOG_LEVEL=INFO
```

### Environment File Priority

The application loads environment variables in this order (later overrides earlier):
1. `.env` (default/template)
2. `.env.local` (your local settings)

**Never commit `.env.local` to version control** - it contains sensitive API keys.

---

## 🎯 Running the Application

### Option 1: Development Mode (Recommended for Development)

#### Terminal 1: Start Frontend Dev Server

```bash
# Navigate to project root (if not already there)
cd c:\Users\shivs\OneDrive\Desktop\gla

# Install dependencies (first time only)
npm install

# Start development server
npm run dev
```

**Output should show:**
```
VITE v6.2.0  ready in 123 ms

➜  Local:   http://localhost:5173/
➜  Press h to show help
```

#### Terminal 2: Start Backend Server

```bash
# Navigate to project root
cd c:\Users\shivs\OneDrive\Desktop\gla

# Activate Python virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Run backend server
python main.py
```

**Output should show:**
```
INFO:     Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
INFO:     Application startup complete
```

#### Access the Application

- **Frontend**: Open browser to [http://localhost:5173](http://localhost:5173)
- **Backend API**: [http://localhost:8001](http://localhost:8001)
- **API Documentation**: [http://localhost:8001/docs](http://localhost:8001/docs) (Swagger UI)
- **Alternative API Docs**: [http://localhost:8001/redoc](http://localhost:8001/redoc) (ReDoc)

### Option 2: Production Build

```bash
# Build frontend
npm run build

# Output will be in dist/ folder

# Run backend in production mode
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Option 3: Docker Deployment (if Dockerfile exists)

```bash
# Build and run with Docker
docker-compose up --build
```

---

## 📚 API Documentation

### Base URL
```
http://localhost:8001/api
```

### Citizen Routes (`/api/citizen`)

#### Analyze Case
```http
POST /api/citizen/analyze-case
Content-Type: application/json

{
  "description": "I had a property dispute with my neighbor...",
  "urgency": "high"
}

Response:
{
  "case_classification": "Civil - Property Law",
  "legal_domain": "Real Estate",
  "primary_issue": "Property Boundary Dispute",
  "legal_summary": "...",
  "probable_remedy": ["Boundary Demarcation", "Monetary Compensation"],
  "suggested_lawyer_type": "Property & Real Estate Lawyer",
  "recommended_lawyers": [...],
  "urgency": "high",
  "portal_recommendation": "District Court"
}
```

#### Request Lawyer
```http
POST /api/citizen/request-lawyer
Content-Type: application/json

{
  "lawyer_id": "profile_123",
  "case_summary": "..."
}

Response: { "status": "success", "request_id": "req_123" }
```

### Chat Routes (`/api/chat`)

#### Chat Summary
```http
POST /api/chat/chat-summary
Content-Type: application/json

{
  "history": [
    { "sender": "user", "text": "..." },
    { "sender": "bot", "text": "..." }
  ]
}

Response: "Summary of the conversation..."
```

#### Legal Draft Generation
```http
POST /api/chat/legal-draft
Content-Type: application/json

{
  "draft_type": "Complaint Petition",
  "case_context": "Property dispute with neighbor",
  "key_points": ["Boundary violation", "Trespassing"]
}

Response: "Legal draft content here..."
```

#### Suggested Next Steps
```http
POST /api/chat/suggested-next-steps
Content-Type: application/json

{
  "history": [...]
}

Response:
{
  "next_steps": ["File case", "Gather evidence", ...],
  "timeline": "2-3 months"
}
```

### Advocate Routes (`/api/advocate`)

#### Precedent Search
```http
GET /api/advocate/search-precedent?query=property+dispute&limit=10

Response:
{
  "results": [
    {
      "case_id": "2023-SCR-456",
      "title": "...",
      "court": "Supreme Court",
      "year": 2023,
      "relevance_score": 0.95
    }
  ]
}
```

#### Build Argument
```http
POST /api/advocate/build-argument
Content-Type: application/json

{
  "case_facts": "...",
  "legal_positions": "...",
  "target_outcome": "..."
}

Response: { "argument": "...", "strength_score": 0.87 }
```

### Judge Routes (`/api/judge`)

#### Case Analysis
```http
POST /api/judge/analyze-case
Content-Type: application/json

{
  "case_id": "2024-DC-789",
  "details": "..."
}

Response:
{
  "consistency_checks": [...],
  "influencing_statutes": [...],
  "bias_detection": [...],
  "key_arguments": {...}
}
```

### Interactive API Explorer

The FastAPI backend automatically generates interactive API documentation:
- **Swagger UI**: http://localhost:8001/docs
- **ReDoc**: http://localhost:8001/redoc

---

## 🧩 Component Guide

### Core Components

#### DashboardLayout
Main layout wrapper for all authenticated views. Manages:
- Navigation sidebar
- Header with user info
- Theme switching
- Language selection

**Props:**
```typescript
interface DashboardLayoutProps {
  userRole: UserRole;
  handleLogout: () => void;
  activeView: ViewType;
  setActiveView: (view: ViewType) => void;
  theme: Theme;
  setTheme: (theme: Theme) => void;
  children: ReactNode;
}
```

#### DisputeInputForm
Collects case details from citizens:
- Text input for case description
- File upload (.txt documents)
- Privacy notice
- Form validation

#### CaseChat
Real-time chat interface for case discussion:
- Message history
- Avatar differentiation
- Timestamp
- Scroll to bottom on new messages

### Visualization Components

#### AnalyticsDashboard
Displays analytics using Chart.js:
- Case statistics
- Success rates
- Timeline charts
- Trend analysis

### Icon Components

The `components/icons/` directory contains 25+ SVG icons:
- `GavelIcon.tsx` - Legal/Justice symbol
- `BellIcon.tsx` - Notifications
- `SearchIcon.tsx` - Search functionality
- `ChatBubbleIcon.tsx` - Messaging
- And many more...

All icons use a consistent interface:
```typescript
interface IconProps {
  className?: string;
  size?: number;
}
```

### Add-on Components

#### BiasMonitor
Detects potential biases in legal reasoning:
- Bias indicators
- Warning messages
- Mitigation suggestions

#### LegalDraftGenerator
Generates legal documents:
- Template selection
- Content customization
- Export options

#### SmartCalendar
Case timeline and deadline management:
- Important dates
- Reminders
- Hearing schedules

---

## 👥 Features by User Role

### Citizen

**Primary Use Case:** File cases and get AI-powered legal guidance

**Key Features:**
1. **Case Filing**
   - Describe case in natural language
   - Upload supporting documents
   - Automatic case classification

2. **AI Analysis**
   - Legal domain identification
   - Probable remedies
   - Case urgency assessment
   - Expected court portal

3. **Lawyer Discovery**
   - Automatic lawyer recommendations
   - Specialization matching
   - Experience verification
   - Direct contact options

4. **Chat & Support**
   - Real-time chat with AI
   - Legal document drafting assistance
   - FAQs and guidance

### Advocate

**Primary Use Case:** Research precedents and build stronger legal arguments

**Key Features:**
1. **Precedent Research**
   - Full-text search across case database
   - Relevance scoring
   - Citation tracking
   - Case summary generation

2. **Argument Building**
   - AI-assisted argument construction
   - Counter-argument generation
   - Legal position strengthening
   - Evidence organization

3. **Analytics & Insights**
   - Case success statistics
   - Judicial behavior patterns
   - Precedent trends
   - Similar case analysis

4. **Performance Tracking**
   - Case outcomes
   - Win rate analysis
   - Client satisfaction metrics

### Judge

**Primary Use Case:** Make informed, transparent, and bias-aware decisions

**Key Features:**
1. **Case Analysis**
   - Comprehensive case summary
   - Key arguments extraction
   - Relevant statutes identification
   - Case complexity assessment

2. **Explainable AI**
   - Transparent AI reasoning
   - Bias detection and alerts
   - Consistency checks
   - Recommendation explanations

3. **Immutable Records**
   - Blockchain-based case logs
   - Tamper-proof records
   - Decision audit trail
   - Reversal history tracking

4. **Judicial Analytics**
   - Case statistics
   - Decision patterns
   - Performance metrics
   - Comparative analysis

---

## 🤖 AI & LLM Integration

### LLM Provider: Groq

The application uses **Groq** as the primary LLM provider via Langchain.

#### Model Configuration
```python
# In app/services/ai_service.py
MODEL_PRIMARY = "llama-3.1-8b-instant"
MODEL_SECONDARY = "llama-3.1-8b-instant"

# Configuration
MAX_INPUT_LENGTH = 6000
DEFAULT_MAX_TOKENS = 2048
```

#### AI Capabilities

1. **Case Analysis**
   - Classify legal domain
   - Identify primary issues
   - Summarize dispute
   - Suggest remedies

2. **Lawyer Recommendations**
   - Select appropriate specializations
   - Match experience level
   - Location-based filtering
   - Success rate analysis

3. **Precedent Analysis**
   - Compare to similar cases
   - Extract relevant principles
   - Identify distinguishing factors

4. **Document Generation**
   - Create legal petitions
   - Draft arguments
   - Generate case summaries
   - Prepare court documents

5. **Chat & Dialogue**
   - Answer legal questions
   - Provide guidance
   - Explain concepts
   - Suggest next steps

### Langchain Integration

The application uses Langchain for:
- LLM prompt structuring
- Message history management
- Response parsing
- Error handling

```python
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=MODEL_PRIMARY,
    temperature=0.7
)

response = llm.invoke([
    SystemMessage(content="You are a legal expert..."),
    HumanMessage(content="User input here")
])
```

### Error Handling & Fallbacks

If Groq API fails:
- Falls back to mock responses
- Logs error details
- Returns sensible defaults
- Maintains user experience

---

## 🔒 Data Privacy & Compliance

### DPDP Act 2023 Compliance

The platform is fully compliant with India's **Digital Personal Data Protection Act, 2023**:

1. **Privacy by Design**
   - Privacy notice on all forms
   - Minimal data collection
   - No sensitive PII required

2. **User Consent**
   - Explicit consent for data processing
   - Privacy notice before submission
   - Clear data usage policies

3. **Data Handling**
   - No storage of sensitive PII
   - Encrypted data transmission
   - Secure API communication
   - Regular security audits

### General Data Protection

1. **Frontend Security**
   - No local storage of sensitive data
   - Secure API communication (HTTPS in production)
   - Token-based authentication

2. **Backend Security**
   - API authentication
   - Input validation
   - SQL injection prevention
   - CORS configuration

3. **API Key Management**
   - Never commit `.env.local` files
   - Use environment variables
   - Rotate keys regularly
   - Monitor API usage

### User Data Policy

- **What we collect**: Case descriptions, dispute details, user preferences
- **What we don't collect**: Full names, addresses, phone numbers, financial details (unless required)
- **How we use it**: AI analysis, legal research, recommendations
- **How we protect it**: Encryption, access controls, regular audits
- **User rights**: Access, correction, deletion upon request

---

## 👨‍💻 Development Guidelines

### Code Structure Best Practices

#### Frontend Components
```typescript
// 1. Imports
import React, { useState, useEffect } from 'react';
import { useTranslations } from '../hooks/useTranslations';
import type { UserRole } from '../types';

// 2. Type Definitions
interface ComponentProps {
  title: string;
  onAction?: () => void;
}

// 3. Component Definition
export function MyComponent({ title, onAction }: ComponentProps) {
  const { t } = useTranslations();
  
  // State
  const [state, setState] = useState(false);
  
  // Effects
  useEffect(() => {
    // Logic here
  }, []);
  
  // Handlers
  const handleClick = () => {
    // Handle action
  };
  
  // Render
  return (
    <div>
      <h1>{t('title')}</h1>
    </div>
  );
}
```

#### Backend Routes
```python
from fastapi import APIRouter, HTTPException
from app.services import ai_service
from app.models import AnalysisResult

router = APIRouter()

@router.post("/analyze")
async def analyze(data: dict) -> AnalysisResult:
    """Analyze case data and return structured result."""
    try:
        # Validate input
        if not data.get('description'):
            raise HTTPException(status_code=400, detail="Missing description")
        
        # Call service
        result = await ai_service.analyze_case(data)
        
        # Return response
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

### Testing

#### Frontend Testing
```bash
# Run tests (if testing framework is added)
npm run test
```

#### Backend Testing
```bash
# Run pytest (add pytest to requirements.txt)
pytest

# With coverage
pytest --cov=app
```

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make changes and commit
git add .
git commit -m "Add feature: description"

# Push and create PR
git push origin feature/your-feature-name
```

### Linting & Formatting

#### Frontend
```bash
# TypeScript compilation check
npx tsc --noEmit

# (Add ESLint if needed)
# npm install --save-dev eslint prettier
```

#### Backend
```bash
# Install linters
pip install flake8 black pylint

# Format code
black app/

# Check style
flake8 app/
pylint app/
```

---

## 🔧 Troubleshooting

### Common Issues & Solutions

#### Frontend Issues

**Issue: "Port 5173 is already in use"**
```bash
# Kill the process using port 5173
# Windows:
netstat -ano | findstr :5173
taskkill /PID <PID> /F

# macOS/Linux:
lsof -ti:5173 | xargs kill -9

# Or use a different port:
npm run dev -- --port 3000
```

**Issue: "Dependencies not installed"**
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

**Issue: "TypeScript compilation errors"**
```bash
# Check types
npx tsc --noEmit

# Update types if needed
npm install --save-dev @types/react @types/react-dom
```

#### Backend Issues

**Issue: "Groq API key not found"**
```bash
# Check .env.local file exists
# Verify GROQ_API_KEY is set
# Check file is not in .gitignore accidentally
```

**Issue: "Port 8001 is already in use"**
```bash
# Windows:
netstat -ano | findstr :8001
taskkill /PID <PID> /F

# macOS/Linux:
lsof -ti:8001 | xargs kill -9

# Or use different port:
python main.py  # Modify port in main.py
```

**Issue: "Failed to import langchain_groq"**
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Or specific package
pip install langchain-groq==0.1.10
```

**Issue: "ModuleNotFoundError: No module named 'app'"**
```bash
# Ensure you're running from project root
cd c:\Users\shivs\OneDrive\Desktop\gla

# Check Python path
python -c "import sys; print(sys.path)"
```

#### CORS Issues

**Error: "Access to XMLHttpRequest has been blocked by CORS policy"**

1. Verify backend CORS configuration in `main.py`
2. Check frontend URL is in `allow_origins`
3. Restart backend server
4. Clear browser cache

#### API Issues

**Error: "Failed to fetch from /api/..."**

```bash
# 1. Verify backend is running
curl http://localhost:8001/health

# 2. Check API endpoint is correct
curl http://localhost:8001/docs

# 3. Verify request format
# Check Content-Type header is application/json
# Check request body is valid JSON
```

### Debugging

#### Frontend Debugging
```typescript
// Add console logs
console.log('Debug info:', data);

// Use browser DevTools
// F12 -> Console, Network, Sources tabs
```

#### Backend Debugging
```python
# Add debug logging
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug(f"Debug info: {data}")

# Use Python debugger
import pdb; pdb.set_trace()
```

### Performance Optimization

#### Frontend
- Use React DevTools Profiler
- Lazy load components with `React.lazy()`
- Optimize images and assets
- Enable CSS minification in production build

#### Backend
- Add database indexing
- Cache frequently used results
- Batch process requests
- Use async operations

---

## 🤝 Contributing

### How to Contribute

1. **Fork the Repository** (if open source)
2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make Your Changes**
   - Follow code style guidelines
   - Add/update tests
   - Update documentation

4. **Commit Your Changes**
   ```bash
   git commit -m "Add amazing feature"
   ```

5. **Push to Branch**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Create a Pull Request**
   - Describe what you changed
   - Reference any related issues
   - Request review from maintainers

### Code Style Guidelines

- **TypeScript**: Follow Google TypeScript Style Guide
- **Python**: Follow PEP 8 style guide
- **Components**: One component per file (if reasonable size)
- **Naming**: Use descriptive, camelCase for JS, snake_case for Python
- **Comments**: Add comments for complex logic

### Testing Requirements

- Add tests for new features
- Ensure existing tests pass
- Aim for >80% code coverage
- Test edge cases and error scenarios

---

## 📞 Support & Contact

For issues, questions, or suggestions:

1. **Check Documentation** - Review this README and code comments
2. **Search Issues** - Check if issue already reported
3. **Create Issue** - Provide detailed description and steps to reproduce
4. **API Docs** - Visit http://localhost:8001/docs for interactive documentation
5. **Community** - Engage with other developers

---

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 🎓 Educational Resources

### Understanding the Technology Stack

- **React**: [Official React Docs](https://react.dev)
- **TypeScript**: [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- **FastAPI**: [FastAPI Documentation](https://fastapi.tiangolo.com/)
- **Langchain**: [Langchain Docs](https://python.langchain.com/)
- **Vite**: [Vite Guide](https://vitejs.dev/guide/)

### Indian Legal System Resources

- [Indian Courts Portal](https://main.sci.gov.in/)
- [Legal Services Authority](https://nalsa.gov.in/)
- [DPDP Act 2023](https://dgft.gov.in/)

---

## 🚀 Future Roadmap

### Planned Features
- [ ] Mobile app (React Native)
- [ ] Advanced analytics dashboard
- [ ] ML-based case outcome prediction
- [ ] Integration with court management systems
- [ ] Multi-party case support
- [ ] Video consultation features
- [ ] Document OCR and parsing
- [ ] Real-time case notifications
- [ ] Advanced search filters
- [ ] Case timeline visualization

### Infrastructure Improvements
- [ ] Docker containerization
- [ ] Kubernetes deployment
- [ ] Database integration (PostgreSQL)
- [ ] Caching layer (Redis)
- [ ] CDN for static assets
- [ ] Monitoring and logging system
- [ ] CI/CD pipeline
- [ ] Security audit

---

## 📈 Project Statistics

- **Frontend Components**: 40+
- **Backend Routes**: 15+
- **Supported Languages**: 7 (English, Hindi, Bengali, Marathi, Tamil, Telugu, Kannada)
- **User Roles**: 3 (Citizen, Advocate, Judge)
- **API Endpoints**: 20+
- **Lines of Code**: 5000+

---

<div align="center">

**Made with ❤️ for Access to Justice**

*Democratizing Legal Intelligence through AI*

[View Repository](#) • [Report Bug](#) • [Request Feature](#) • [Get Help](#)

</div>

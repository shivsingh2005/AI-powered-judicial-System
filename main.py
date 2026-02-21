"""
FastAPI backend for AI Justice Hub
Replaces the TypeScript Gemini service with Python Langchain + Groq
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import routes
from app.routes import citizen, advocate, judge, chat

app = FastAPI(
    title="AI Justice Hub API",
    description="Backend API for AI Justice Hub using Langchain and Groq",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(citizen.router, prefix="/api/citizen", tags=["Citizen"])
app.include_router(advocate.router, prefix="/api/advocate", tags=["Advocate"])
app.include_router(judge.router, prefix="/api/judge", tags=["Judge"])
app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])

@app.get("/")
async def root():
    return {"message": "AI Justice Hub API is running", "status": "healthy"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "AI Justice Hub"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)

"""
Chat API Routes
"""
from fastapi import APIRouter, HTTPException, Body
from app.services import ai_service
from app.models import NextStepsResponse
from typing import List, Dict

router = APIRouter()

@router.post("/chat-summary")
async def get_chat_summary(history: List[Dict[str, str]] = Body(...)) -> str:
    """Summarize a legal chat history."""
    try:
        result = await ai_service.get_chat_summary(history)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/suggested-next-steps")
async def get_suggested_next_steps(history: List[Dict[str, str]] = Body(...)) -> NextStepsResponse:
    """Suggest next steps for a legal chat."""
    try:
        result = await ai_service.get_suggested_next_steps(history)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/legal-draft")
async def generate_legal_draft(data: dict = Body(...)) -> str:
    """Generate a professional legal draft for India."""
    try:
        draft_type = data.get('draft_type', '')
        case_context = data.get('case_context', '')
        key_points = data.get('key_points', '')
        result = await ai_service.generate_legal_draft(draft_type, case_context, key_points)
        return result
    except Exception as e:
        import traceback
        print(f"Error in generate_legal_draft: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/bias-monitor")
async def monitor_bias(data: dict = Body(...)):
    """Analyze document for judicial bias or hallucinations."""
    try:
        document_text = data.get('document_text', '')
        result = await ai_service.monitor_for_bias(document_text)
        return result
    except Exception as e:
        import traceback
        print(f"Error in monitor_bias: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))

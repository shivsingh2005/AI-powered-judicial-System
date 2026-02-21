"""
Judge API Routes
"""
from fastapi import APIRouter, HTTPException, Body
from app.services import ai_service
from app.models import PrecedentAnalysisResult

router = APIRouter()

@router.post("/precedent-analysis")
async def get_precedent_analysis(data: dict = Body(...)) -> PrecedentAnalysisResult:
    """Analyze a judgment for key arguments, influencing statutes, and logical consistency."""
    try:
        document_text = data.get('document_text', '')
        result = await ai_service.get_precedent_analysis(document_text)
        return result
    except Exception as e:
        import traceback
        print(f"Error in get_precedent_analysis: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))

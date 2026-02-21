"""
Citizen API Routes
"""
from fastapi import APIRouter, HTTPException, Body
from app.services import ai_service
from app.models import CitizenAnalysisResult, RAGResult

router = APIRouter()

@router.post("/analyze-dispute")
async def analyze_dispute(data: dict = Body(...)) -> CitizenAnalysisResult:
    """Analyze an Indian legal dispute and provide structured analysis."""
    try:
        dispute_text = data.get('dispute_text', '')
        result = await ai_service.analyze_dispute(dispute_text)
        return result
    except Exception as e:
        import traceback
        print(f"Error in analyze_dispute: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/rag-search")
async def rag_search(data: dict = Body(...)) -> RAGResult:
    """Perform RAG search on document text."""
    try:
        query = data.get('query', '')
        document_text = data.get('document_text', '')
        result = await ai_service.perform_rag_search(query, document_text)
        return result
    except Exception as e:
        import traceback
        print(f"Error in rag_search: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/case-requests")
async def get_case_requests():
    """Generate and return realistic case requests for advocates."""
    try:
        result = await ai_service.generate_case_requests(count=4)
        # Extract the array from the result if it's wrapped
        if isinstance(result, dict) and isinstance(result.get(''), list):
            return result['']
        elif isinstance(result, list):
            return result
        # If the LLM returned wrapped JSON, extract the array
        return result
    except Exception as e:
        import traceback
        print(f"Error in get_case_requests: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))

        import traceback
        print(f"Error in rag_search: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))

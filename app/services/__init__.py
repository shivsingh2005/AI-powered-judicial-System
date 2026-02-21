"""
AI Services module
"""
from app.services.ai_service import (
    analyze_dispute,
    perform_rag_search,
    get_precedent_analysis,
    get_similar_cases,
    get_llm_manager,
)

# For backwards compatibility with route imports
import app.services.ai_service as ai_service

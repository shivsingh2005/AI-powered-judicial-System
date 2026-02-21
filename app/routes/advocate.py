"""
Advocate API Routes
"""
from fastapi import APIRouter, HTTPException, Body
from app.services import ai_service
from app.models import SimilarCaseAnalysisResult, ArgumentBuilderResult, AIResearchPipelineResult, SimilarCase, SimilarCaseResearch, RAGResearchResult

router = APIRouter()

@router.post("/similar-cases")
async def get_similar_cases(data: dict = Body(...)) -> SimilarCaseAnalysisResult:
    """Find similar fictional Indian case laws for given facts."""
    try:
        case_facts = data.get('case_facts', '')
        result = await ai_service.get_similar_cases(case_facts)
        # Normalize different possible LLM return shapes into expected list
        similar_cases_list = []
        raw_list = []
        if isinstance(result, dict):
            # prefer explicit field
            if 'similar_cases_found' in result and isinstance(result.get('similar_cases_found'), list):
                raw_list = result.get('similar_cases_found')
            else:
                # maybe LLM returned top-level keys for a single case
                # attempt to detect a single-case dict
                if all(k in result for k in ('case_title', 'summary_of_decision')):
                    raw_list = [result]
        elif isinstance(result, list):
            raw_list = result
        else:
            # Unexpected shape — log for debugging and raise a friendly error
            import traceback
            print(f"Unexpected similar-cases response shape: {type(result)}\n{result}")
            raise ValueError('Invalid response shape from LLM for similar cases')

        # Build typed SimilarCase objects with safe coercions
        for case in raw_list:
            try:
                relevance = case.get('relevance_score', case.get('score', 0.0)) if isinstance(case, dict) else 0.0
                try:
                    relevance = float(relevance)
                except Exception:
                    relevance = 0.0
                similar_cases_list.append(SimilarCase(
                    case_title=(case.get('case_title') if isinstance(case, dict) else str(case)),
                    citation_or_year=(case.get('citation_or_year', case.get('citation', 'Unknown')) if isinstance(case, dict) else 'Unknown'),
                    court_name=(case.get('court_name', 'Unknown Court') if isinstance(case, dict) else 'Unknown Court'),
                    summary_of_decision=(case.get('summary_of_decision', '') if isinstance(case, dict) else ''),
                    relevance_score=relevance,
                    key_sections_cited=(case.get('key_sections_cited', []) if isinstance(case, dict) else []),
                    legal_takeaway=(case.get('legal_takeaway', '') if isinstance(case, dict) else '')
                ))
            except Exception:
                # Skip malformed entries but continue processing others
                import traceback
                print(f"Skipping malformed similar-case entry: {traceback.format_exc()}")
        
        # Build response with proper structure
        # populate top-level metadata defensively
        role = result.get('role') if isinstance(result, dict) and 'role' in result else 'Advocate'
        feature = result.get('feature') if isinstance(result, dict) and 'feature' in result else 'Similar Case Analyzer'
        case_context_summary = result.get('case_context_summary') if isinstance(result, dict) and 'case_context_summary' in result else ''
        overall_summary = result.get('overall_summary') if isinstance(result, dict) and 'overall_summary' in result else ''
        suggested_action = result.get('suggested_action') if isinstance(result, dict) and 'suggested_action' in result else ''

        response = SimilarCaseAnalysisResult(
            role=role,
            feature=feature,
            case_context_summary=case_context_summary,
            similar_cases_found=similar_cases_list,
            overall_summary=overall_summary,
            suggested_action=suggested_action
        )
        return response
    except Exception as e:
        import traceback
        print(f"Error in get_similar_cases: {traceback.format_exc()}")
        # Return a friendly message while preserving logs for debugging
        raise HTTPException(status_code=500, detail='An error occurred while finding similar cases. The AI model may have returned an invalid response. Please try again.')

@router.post("/generate-arguments")
async def generate_arguments(data: dict = Body(...)) -> ArgumentBuilderResult:
    """Build a legal argument for plaintiff or defendant."""
    try:
        case_facts = data.get('case_facts', '')
        desired_outcome = data.get('desired_outcome', '')
        legal_stance = data.get('legal_stance', '')
        result = await ai_service.generate_arguments(case_facts, desired_outcome, legal_stance)
        return result
    except Exception as e:
        import traceback
        print(f"Error in generate_arguments: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/ai-research")
async def get_ai_research(data: dict = Body(...)) -> AIResearchPipelineResult:
    """Synthesize research from multiple sources."""
    try:
        case_facts = data.get('case_facts', '')
        similar_cases = data.get('similar_cases', {})
        rag_result = data.get('rag_result', {})
        result = await ai_service.get_ai_research_summary(case_facts, similar_cases, rag_result)
        
        # Extract similar cases with required fields
        similar_cases_list = []
        if isinstance(similar_cases, dict) and 'similar_cases_found' in similar_cases:
            for case in similar_cases.get('similar_cases_found', []):
                similar_cases_list.append(SimilarCaseResearch(
                    case_title=case.get('case_title', 'Unknown Case'),
                    court_name=case.get('court_name', 'Unknown Court'),
                    citation=case.get('citation_or_year', str(case.get('year', 'Unknown'))),
                    relevance_score=float(case.get('relevance_score', 0.0))
                ))
        
        # Extract RAG results with required fields
        rag_results_list = []
        if isinstance(rag_result, dict):
            if 'answers' in rag_result:
                rag_results_list.append(RAGResearchResult(
                    section='Answer',
                    summary=rag_result.get('answers', rag_result.get('answer', ''))
                ))
            elif 'answer' in rag_result:
                rag_results_list.append(RAGResearchResult(
                    section='Answer',
                    summary=rag_result.get('answer', '')
                ))
        
        # Build the final response
        pipeline_result = AIResearchPipelineResult(
            pipeline_stage='Complete',
            case_context=case_facts,
            similar_cases=similar_cases_list,
            rag_results=rag_results_list,
            final_summary=result.get('final_summary', result.get('case_summary', '')),
            argument_suggestion=result.get('argument_suggestion', result.get('strongest_arguments', [{}])[0].get('description', ''))
        )
        
        return pipeline_result
    except Exception as e:
        import traceback
        print(f"Error in get_ai_research: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))

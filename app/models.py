"""
Pydantic models for AI Justice Hub API
These match the TypeScript types defined in types.ts
"""
from pydantic import BaseModel, Field
from typing import List, Optional, Union

# ==================== Citizen Models ====================

class RecommendedLawyer(BaseModel):
    name: str
    specialization: str
    experience_years: int
    success_rate: Union[str, int] = "N/A"
    location: str
    profile_id: str
    contact_option: str

class CitizenAnalysisResult(BaseModel):
    case_classification: str
    legal_domain: str
    primary_issue: str
    legal_summary: str
    probable_remedy: List[str]
    suggested_lawyer_type: str
    recommended_lawyers: List[RecommendedLawyer]
    lawyer_request_summary: str
    urgency: str
    portal_recommendation: str

class RAGResult(BaseModel):
    answer: str
    citations: List[str]

# ==================== Judge Models ====================

class InfluencingStatute(BaseModel):
    statute: str
    quote: str
    relevance: str

class ConsistencyCheck(BaseModel):
    issue: str
    explanation: str

class BiasDetection(BaseModel):
    warning: str

class KeyArguments(BaseModel):
    plaintiff: str
    defendant: str

class PrecedentAnalysisResult(BaseModel):
    keyArguments: KeyArguments
    influencingStatutes: List[InfluencingStatute]
    consistencyCheck: List[ConsistencyCheck]
    biasDetection: BiasDetection

# ==================== Advocate Models ====================

class SimilarCase(BaseModel):
    case_title: str
    citation_or_year: str
    court_name: str
    summary_of_decision: str
    relevance_score: float
    key_sections_cited: List[str]
    legal_takeaway: str

class SimilarCaseAnalysisResult(BaseModel):
    role: str = "Advocate"
    feature: str = "Similar Case Analyzer"
    case_context_summary: str
    similar_cases_found: List[SimilarCase]
    overall_summary: str
    suggested_action: str

class SupportingPoint(BaseModel):
    point: str
    explanation: str

class CounterArgument(BaseModel):
    argument: str
    rebuttal: str

class ArgumentBuilderResult(BaseModel):
    core_argument: str
    supporting_points: List[SupportingPoint]
    potential_counter_arguments: List[CounterArgument]
    evidence_checklist: List[str]
    suggested_precedents: List[str]

# ==================== Chat Models ====================

class CaseChatMessage(BaseModel):
    id: str
    caseId: str
    role: str
    text: str
    timestamp: str

class NextStepsResponse(BaseModel):
    suggestions: List[str]
    clarification_needed: Optional[str] = None

# ==================== AI Research Models ====================

class SimilarCaseResearch(BaseModel):
    case_title: str
    court_name: str
    citation: str
    relevance_score: float

class RAGResearchResult(BaseModel):
    section: str
    summary: str

class AIResearchPipelineResult(BaseModel):
    pipeline_stage: str = "Complete"
    case_context: str
    similar_cases: List[SimilarCaseResearch]
    rag_results: List[RAGResearchResult]
    final_summary: str
    argument_suggestion: str

# ==================== Bias Analysis Models ====================

class BiasFinding(BaseModel):
    phrase: str
    bias_type: str
    explanation: str
    suggestion: str

class BiasAnalysisResult(BaseModel):
    has_bias: bool
    findings: List[BiasFinding]

# ==================== Legal Draft Models ====================

class LegalDraftRequest(BaseModel):
    draft_type: str
    case_context: str
    key_points: str

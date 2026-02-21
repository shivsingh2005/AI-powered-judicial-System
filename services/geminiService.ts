// Backend API service for AI Justice Hub
// Connects to FastAPI backend

import type { 
  SimilarCaseAnalysisResult, 
  RAGResult, 
  PrecedentAnalysisResult,
  CitizenAnalysisResult,
  ArgumentBuilderResult,
  AIResearchPipelineResult,
  NextStepsResponse
} from '../types';
import type { Chat } from '@google/genai';

const API_BASE_URL = 'http://localhost:8001/api';

// Helper function to make API calls
async function apiCall<T>(endpoint: string, body: any): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: typeof body === 'string' ? JSON.stringify(body) : JSON.stringify(body),
  });

  if (!response.ok) {
    throw new Error(`API call failed: ${response.statusText}`);
  }

  return response.json();
}

// SimilarCaseAnalyzer - calls advocate/similar-cases endpoint
export async function getSimilarCases(caseFacts: string): Promise<SimilarCaseAnalysisResult> {
  return apiCall<SimilarCaseAnalysisResult>('/advocate/similar-cases', { case_facts: caseFacts });
}

// PrecedentSearch - calls citizen/rag-search endpoint
export async function performRAGSearch(query: string, documentText: string = ''): Promise<RAGResult> {
  // If documentText is not provided, use a default context
  const docText = documentText || 'Legal document for search';
  return apiCall<RAGResult>('/citizen/rag-search', { query, document_text: docText });
}

// ExplainableAI - calls judge/precedent-analysis endpoint
export async function getPrecedentAnalysis(documentText: string): Promise<PrecedentAnalysisResult> {
  return apiCall<PrecedentAnalysisResult>('/judge/precedent-analysis', { document_text: documentText });
}

// Judicial Analytics - calls judge/analytics endpoint
export async function getJudicialAnalytics(caseContext: string, timeframe: string = 'last_5_years'): Promise<any> {
  return apiCall<any>('/judge/analytics', { case_context: caseContext, timeframe });
}

// CitizenDashboard - calls citizen/analyze-dispute endpoint
export async function analyzeDispute(disputeDescription: string): Promise<CitizenAnalysisResult> {
  return apiCall<CitizenAnalysisResult>('/citizen/analyze-dispute', { dispute_text: disputeDescription });
}

// Chatbot - returns a mock Chat object (for now, using stub)
export function createChatSession(systemInstruction: string): Chat {
  console.warn('createChatSession is using a stub implementation');
  // Return a minimal mock object
  return {
    sendMessageStream: async function* (_request: { message: string }) {
      yield { text: 'This is a stub implementation. Please connect to Google AI.' };
    }
  } as unknown as Chat;
}

// CaseRequests - calls chat/chat-summary endpoint
export async function getChatSummary(history: {role: string, text: string}[]): Promise<string> {
  return apiCall<string>('/chat/chat-summary', history);
}

export async function getSuggestedNextSteps(history: {role: string, text: string}[]): Promise<NextStepsResponse> {
  return apiCall<NextStepsResponse>('/chat/suggested-next-steps', history);
}

// ArgumentBuilder - calls advocate/generate-arguments endpoint
export async function generateArguments(
  caseFacts: string, 
  desiredOutcome: string, 
  legalStance: string
): Promise<ArgumentBuilderResult> {
  return apiCall<ArgumentBuilderResult>('/advocate/generate-arguments', {
    case_facts: caseFacts,
    desired_outcome: desiredOutcome,
    legal_stance: legalStance
  });
}

// AIResearchHub - calls advocate/ai-research endpoint
export async function getAIResearchSummary(
  caseContext: string,
  similarCases: any,
  ragResult: any
): Promise<AIResearchPipelineResult> {
  return apiCall<AIResearchPipelineResult>('/advocate/ai-research', {
    case_facts: caseContext,
    similar_cases: similarCases,
    rag_result: ragResult
  });
}

// Legal draft generation - calls chat/legal-draft endpoint
export async function generateLegalDraft(
  draftType: string,
  caseContext: string,
  keyPoints: string
): Promise<string> {
  return apiCall<string>('/chat/legal-draft', {
    draft_type: draftType,
    case_context: caseContext,
    key_points: keyPoints
  });
}

// Bias monitor - calls chat/bias-monitor endpoint
export async function monitorBias(documentText: string): Promise<any> {
  return apiCall<any>('/chat/bias-monitor', { document_text: documentText });
}

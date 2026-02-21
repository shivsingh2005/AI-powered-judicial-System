import React, { useState, useEffect } from 'react';
import type { CaseRequest, CaseChatMessage } from '../types';
import { RequestCard } from './RequestCard';
import { CaseChat } from './CaseChat';
import { getChatSummary, getSuggestedNextSteps } from '../services/geminiService';
import { ChatIcon } from './icons/ChatIcon';
import { useTranslations } from '../hooks/useTranslations';

export const CaseRequests: React.FC = () => {
  const [requests, setRequests] = useState<CaseRequest[]>([]);
  const [chatHistories, setChatHistories] = useState<Record<string, CaseChatMessage[]>>({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [chattingCase, setChattingCase] = useState<CaseRequest | null>(null);
  const t = useTranslations();

  useEffect(() => {
    // Fetch case requests from API
    const fetchCaseRequests = async () => {
      try {
        setLoading(true);
        setError(null);
        const response = await fetch('http://localhost:8001/api/citizen/case-requests', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        
        if (!response.ok) {
          throw new Error(`Failed to fetch case requests: ${response.statusText}`);
        }
        
        const data = await response.json();
        // Handle both array and wrapped responses
        const caseRequests = Array.isArray(data) ? data : data.requests || [];
        setRequests(caseRequests);
      } catch (err) {
        console.error('Error fetching case requests:', err);
        setError(err instanceof Error ? err.message : 'Failed to load case requests');
      } finally {
        setLoading(false);
      }
    };

    fetchCaseRequests();
  }, []);

  const handleUpdateRequest = (requestId: string, newStatus: 'Accepted' | 'Rejected') => {
    setRequests(prevRequests =>
      prevRequests.map(req =>
        req.id === requestId ? { ...req, status: newStatus } : req
      )
    );
  };

  const handleOpenChat = (caseId: string) => {
    const caseToChat = requests.find(c => c.id === caseId);
    if (caseToChat) {
      setChattingCase(caseToChat);
    }
  };

  const handleSendMessage = (text: string) => {
    if (!chattingCase) return;

    const newMessage: CaseChatMessage = {
        id: `msg-${Date.now()}`,
        caseId: chattingCase.id,
        role: 'advocate',
        text,
        timestamp: new Date().toISOString(),
    };
    
    const updatedHistory = [...(chatHistories[chattingCase.id] || []), newMessage];
    setChatHistories(prev => ({...prev, [chattingCase.id]: updatedHistory }));

    // Use LLM to generate realistic citizen response through API if available
    // For now, simulate a response
    setTimeout(() => {
        const citizenReply: CaseChatMessage = {
            id: `msg-${Date.now() + 1}`,
            caseId: chattingCase.id,
            role: 'citizen',
            text: "Thank you for the guidance. I will follow the recommended steps and keep you updated.",
            timestamp: new Date().toISOString(),
        };
        setChatHistories(prev => ({...prev, [chattingCase.id]: [...updatedHistory, citizenReply] }));
    }, 2500);
  };

  const pendingRequests = requests.filter(r => r.status === 'Pending');
  const handledRequests = requests.filter(r => r.status !== 'Pending');

  return (
    <div className="grid grid-cols-1 lg:grid-cols-5 gap-6" style={{ height: 'calc(100vh - 150px)'}}>
        <div className="lg:col-span-2 overflow-y-auto pr-2">
            <h1 className="text-2xl font-bold text-[rgb(var(--foreground))] mb-1">{t.caseRequests.title}</h1>
            <p className="text-[rgb(var(--muted-foreground))] mb-6">{t.caseRequests.description}</p>

            {loading ? (
                <p>{t.caseRequests.loading}</p>
            ) : error ? (
                <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
                    <p className="font-bold">Error</p>
                    <p>{error}</p>
                </div>
            ) : (
                <div className="space-y-6">
                <div>
                    <h2 className="text-lg font-semibold text-[rgb(var(--card-foreground))] mb-3">{t.caseRequests.pending} ({pendingRequests.length})</h2>
                    {pendingRequests.length > 0 ? (
                        <div className="space-y-4">
                        {pendingRequests.map(request => (
                            <RequestCard 
                                key={request.id} 
                                request={request} 
                                onAccept={() => handleUpdateRequest(request.id, 'Accepted')}
                                onReject={() => handleUpdateRequest(request.id, 'Rejected')}
                            />
                        ))}
                        </div>
                    ) : (
                        <div className="bg-[rgb(var(--card))] border border-[rgb(var(--border))] rounded-lg p-6 text-center">
                            <p className="text-[rgb(var(--muted-foreground))]">{t.caseRequests.noPending}</p>
                        </div>
                    )}
                </div>
                <div>
                    <h2 className="text-lg font-semibold text-[rgb(var(--card-foreground))] mb-3">{t.caseRequests.handled} ({handledRequests.length})</h2>
                    {handledRequests.length > 0 ? (
                        <div className="space-y-4">
                        {handledRequests.map(request => (
                            <RequestCard 
                                key={request.id} 
                                request={request} 
                                onOpenChat={handleOpenChat}
                            />
                        ))}
                        </div>
                    ) : (
                        <div className="bg-[rgb(var(--card))] border border-[rgb(var(--border))] rounded-lg p-6 text-center">
                            <p className="text-[rgb(var(--muted-foreground))]">{t.caseRequests.noHandled}</p>
                        </div>
                    )}
                </div>
                </div>
            )}
        </div>
        <div className="lg:col-span-3 h-full">
            {chattingCase ? (
                <CaseChat
                caseRequest={chattingCase}
                messages={chatHistories[chattingCase.id] || []}
                currentUserRole="advocate"
                onClose={() => setChattingCase(null)}
                onSendMessage={handleSendMessage}
                getSummary={getChatSummary}
                getSuggestedNextSteps={getSuggestedNextSteps}
                />
            ) : (
                <div className="bg-[rgb(var(--card))] border-2 border-dashed border-[rgb(var(--border))] rounded-lg h-full flex flex-col items-center justify-center text-center p-4">
                    <ChatIcon className="w-16 h-16 text-[rgb(var(--muted-foreground))]"/>
                    <h3 className="mt-4 text-lg font-semibold text-[rgb(var(--card-foreground))]">{t.caseRequests.chatTitle}</h3>
                    <p className="mt-1 text-sm text-[rgb(var(--muted-foreground))]">{t.caseRequests.chatDescription}</p>
                </div>
            )}
        </div>
    </div>
  );
};
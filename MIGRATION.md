# Migration Guide: From Mock Data to LLM-Only Architecture

## Overview

This document outlines all changes made to migrate from a mock data-based system to a fully LLM-powered system using Groq API.

## Backend Changes (Python/FastAPI)

### `app/services/ai_service.py`

**Removed:**
- All `get_mock_*()` functions:
  - `get_mock_dispute_analysis()`
  - `get_mock_similar_cases()`
  - `get_mock_arguments()`
  - `get_mock_ai_research()`
  - `get_mock_next_steps()`
  - `get_mock_legal_draft()`
  - `get_mock_bias_analysis()`

**Changed:**
- `LLMManager.__init__()`: Now requires valid `GROQ_API_KEY` and raises `ValueError` if not available
- `invoke_json_llm()`: Removed `mock_fallback` parameter; now always requires valid LLM
- All service functions: Removed early returns for missing API keys and mock_fallback calls
  - `analyze_dispute()`
  - `perform_rag_search()`
  - `get_precedent_analysis()`
  - `get_similar_cases()`
  - `generate_arguments()`
  - `get_ai_research_summary()`
  - `get_chat_summary()`
  - `get_suggested_next_steps()`
  - `generate_legal_draft()`
  - `monitor_for_bias()`

**Added:**
- `generate_case_requests()`: New function to dynamically generate realistic case requests using LLM

### `app/routes/citizen.py`

**Added:**
- `GET /case-requests`: New endpoint to fetch LLM-generated case requests for advocates

## Frontend Changes (TypeScript/React)

### `data/mockData.ts`

**Changed:**
- Deprecated all mock data
- File now exports empty arrays with deprecation notice
- Existing imports still work (for compatibility) but return empty data

### `components/CaseRequests.tsx`

**Removed:**
- Import of `initialCaseRequests` and `initialChatHistories` from mockData
- Simulated API fetch using `setTimeout`

**Added:**
- Real API call to `GET /api/citizen/case-requests`
- Async `fetchCaseRequests()` function
- Error state handling
- Loading state management

### `components/AIResearchHub.tsx`

**Removed:**
- `mockRagResult` constant (was unused)
- Comment about mocking RAG results for consistency

### `components/LiveCaseFeed.tsx`

**Updated:**
- Comment changed from "Mock data" to "TODO: Generate feed items dynamically using LLM"
- Static data marked as demonstration only

### `components/BlockchainLog.tsx`

**Updated:**
- Comment changed from "Mock data" to "TODO: Generate log items dynamically using LLM"
- Static data marked as demonstration only

### `components/addons/SmartCalendar.tsx`

**Updated:**
- Comment changed from "Mock data for calendar events" to "TODO: Generate calendar events dynamically"
- Static data marked as demonstration only

## API Endpoints

### All existing endpoints now:
1. Require valid `GROQ_API_KEY` environment variable
2. Will raise HTTP 500 errors if LLM calls fail
3. Never fall back to mock data

### New endpoints:
- `GET /api/citizen/case-requests` - Generates realistic case requests via LLM

### Future endpoints to implement:
- `GET /api/live-feed/generate` - Generate live case feed items
- `GET /api/blockchain/generate` - Generate blockchain log entries
- `GET /api/calendar/generate` - Generate calendar events

## Error Handling

### Before:
- Missing API key → silent fallback to mocks
- LLM errors → fallback to mocks
- User experiences placeholder data without knowing it's mock

### After:
- Missing API key → Clear `ValueError` at startup
- LLM errors → HTTP 500 with detailed error message
- User knows immediately if service is unavailable
- All content is production-ready (no mocks)

## Configuration

### Required Environment Variables

```env
GROQ_API_KEY=your_groq_api_key
```

### Optional Environment Variables

```env
VITE_API_URL=http://localhost:8001/api  # Frontend API URL
```

## Testing

### Unit Tests
- All mock-dependent tests should be updated
- Test functions that now require API key should mock the LLMManager

### Integration Tests
- Should use real Groq API or mock it at the HTTP level
- Backend should be running to test API endpoints

### Manual Testing

1. **Case Requests Loading:**
   ```
   Visit advocate dashboard
   Should see dynamically generated case requests from LLM
   ```

2. **Dispute Analysis:**
   ```
   Fill in DisputeInputForm
   Submit → Should get LLM-generated analysis
   ```

3. **Similar Cases:**
   ```
   Use similar case analyzer
   Should return LLM-generated realistic precedent cases
   ```

## Breaking Changes

1. **API will fail if `GROQ_API_KEY` is not set**
   - Previously: Silently used mocks
   - Now: Raises error immediately

2. **Mock data files are deprecated**
   - `mockData.ts` exports empty data
   - Any code importing from it will get empty arrays

3. **All functions require valid LLM client**
   - No fallback behavior
   - Errors are propagated to frontend

## Rollback Instructions

To restore mock data behavior (not recommended):

1. Restore original `mockData.ts` from git history
2. Restore original `ai_service.py` functions
3. Revert component changes to use mock imports

## Performance Considerations

1. **Groq API calls are slower than mocks**
   - Allow extra time for responses (typically 1-5 seconds)
   - Consider adding spinner/loading states

2. **Rate limiting**
   - Groq has API rate limits based on tier
   - Monitor usage to avoid hitting limits

3. **Cost**
   - Groq API is pay-as-you-go
   - Keep track of API usage vs. expected costs

## Validation

After migration, verify:

✅ No imports of mock data remain in active components
✅ All API endpoints return LLM-generated content
✅ Error messages are clear and actionable
✅ Environment variables are properly documented
✅ No hardcoded test data in production code
✅ Loading states show while LLM processes requests

## Future Improvements

1. Add caching for frequently requested analyses
2. Implement rate limiting on backend
3. Add fallback to different LLM provider if Groq fails
4. Store used responses in database for auditing
5. Add response validation to ensure output quality
6. Implement WebSocket for real-time updates
7. Add batch processing for multiple requests

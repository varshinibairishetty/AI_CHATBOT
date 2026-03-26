from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn
from ai_agent import get_response_from_ai_agent

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

app = FastAPI(title="AI Agent Node")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    try:
        # Extract the user's message
        query_text = request.messages[0] if request.messages else ""

        # Get response from our agent logic
        response = get_response_from_ai_agent(
            llm_id=request.model_name,
            query=query_text,
            allow_search=request.allow_search,
            system_prompt=request.system_prompt,
            provider=request.model_provider
        )
        
        return {"reply": response}
    
    except Exception as e:
        # Return the error message to the frontend for debugging
        return {"reply": f"Error: {str(e)}"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9999)
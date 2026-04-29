# backend/routes/ask.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os

# Import your agent
from agent.agent_pipeline import agent_pipeline

router = APIRouter()

# Request Schema
class QueryRequest(BaseModel):
    query: str
    user_id: str = "default_user1"


@router.post("/ask")
def ask_question(request: QueryRequest):
    """
    Handle user queries using Agent
    """

    # Step 1: Check if vector DB exists
    if not os.path.exists("vectorstore"):
        raise HTTPException(
            status_code=400,
            detail="Please upload at least 1 PDF first"
        )

    try:
        # Step 2: Call agent pipeline
        result = agent_pipeline(
            query=request.query,
            user_id=request.user_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing query: {str(e)}"
        )

    # Step 3: Return structured response
    return {
        "query": request.query,
        "answer": result.get("answer"),
        "tool_used": result.get("tool_used"),
        "type": result.get("type")
    }


#in return section of API call right most part should be same to the left most side of return part of backend part.
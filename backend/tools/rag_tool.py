from dotenv import load_dotenv
import os

load_dotenv()


from rag.rag_pipeline import rag_query

def rag_tool(query, chat_history=None):
    """
    RAG Tool:
    - Takes user query
    - Fetches answer from RAG pipeline
    - Returns structured output
    """

    try:
        # Call RAG pipeline
        answer = rag_query(query)

        return {
            "tool": "rag",
            "answer": answer,
            "sources": None   # optional (can add later)
        }

    except Exception as e:
        return {
            "tool": "rag",
            "answer": f"Error: {str(e)}",
            "sources": None
        }
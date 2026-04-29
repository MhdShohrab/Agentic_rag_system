from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

from langchain_groq import ChatGroq

def llm_tool(query, chat_history=None):
    """
    General purpose LLM tool
    """

    try:
        llm = ChatGroq(
            model_name="llama-3.1-8b-instant",
            temperature=0.5
        )

        prompt = f"""
        You are a helpful AI assistant.

        Chat history:
        {chat_history}

        User question:
        {query}
        """

        response = llm.invoke(prompt)

        return {
            "tool": "llm",
            "answer": response.content
        }

    except Exception as e:
        return {
            "tool": "llm",
            "answer": f"Error: {str(e)}"
        }
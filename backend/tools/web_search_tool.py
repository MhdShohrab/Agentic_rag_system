from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

from tavily import TavilyClient
from langchain_groq import ChatGroq
import os

def web_search_tool(query, chat_history=None):
    """
    Fetch latest information from web
    """

    try:
        tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

        results = tavily.search(query=query, max_results=3)

        content = "\n\n".join([r["content"] for r in results["results"]])

        llm = ChatGroq(
            model_name="llama-3.1-8b-instant",
            temperature=0.3
        )

        prompt = f"""
        Based on the following web results, answer the question:

        {content}

        Question:
        {query}
        """

        response = llm.invoke(prompt)

        return {
            "tool": "web",               # for future ->from where the answer is generated 
            "answer": response.content
        }

    except Exception as e:
        return {
            "tool": "web",
            "answer": f"Error: {str(e)}"
        }
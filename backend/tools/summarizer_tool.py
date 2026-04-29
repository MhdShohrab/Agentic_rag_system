from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

from rag.vectorstore import load_vector_db
from rag.retriever import retrieve_docs
from langchain_groq import ChatGroq

def summarizer_tool(query, chat_history=None):
    """
    Summarizes document content
    """

    try:
        vector_db = load_vector_db()

        docs = retrieve_docs(vector_db, query, k=5)

        context = "\n\n".join([doc.page_content for doc in docs])

        llm = ChatGroq(
            model_name="llama-3.1-8b-instant",
            temperature=0.3
        )

        prompt = f"""
        Summarize the following content:

        {context}
        """

        response = llm.invoke(prompt)

        return {
            "tool": "summarizer",
            "answer": response.content
        }

    except Exception as e:
        return {
            "tool": "summarizer",
            "answer": f"Error: {str(e)}"
        }
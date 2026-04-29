# backend/agent/decision.py
# (decide which tool to be used for which querry) Hybrid Decision System
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import re        #regular expression

load_dotenv(dotenv_path="backend/.env")

def is_math_query(query):
    """
    Detect math queries
    """
    return bool(re.search(r"\d+\s*[\+\-\*/]\s*\d+", query))


def is_web_query(query):
    """
    Detect latest / real-time queries
    """
    keywords = ["latest", "news", "today", "current", "recent"]
    return any(word in query.lower() for word in keywords)


def is_rag_query(query):
    """
    Detect document-related queries
    """
    keywords = ["document", "pdf", "file", "report"]
    return any(word in query.lower() for word in keywords)


def is_summarizer_query(query):
    """
    Detect summarization requests
    """
    keywords = ["summarize", "summary", "gist", "brief"]
    return any(word in query.lower() for word in keywords)


def decide_tool(query, chat_history=None):
    """
    Hybrid Decision System:
    Rule-based → LLM fallback
    """

    query_lower = query.lower()

    # PRIORITY 1: CALCULATOR
    if is_math_query(query):
        return "calculator"

    # PRIORITY 2: WEB SEARCH
    if is_web_query(query):
        return "web"

    # PRIORITY 3: RAG
    if is_rag_query(query):
        return "rag"

    # PRIORITY 4: SUMMARIZER
    if is_summarizer_query(query):
        return "summarizer"

    # FALLBACK: LLM DECISION
    llm = ChatGroq(
        model_name="llama-3.1-8b-instant",
        temperature=0
    )

    prompt = f"""
    You are an AI agent.

    Available tools:
    - rag → document questions
    - calculator → math
    - web → latest info
    - summarizer → summarize content
    - llm → general knowledge

    Return ONLY tool name.

    Question: {query}
    """

    response = llm.invoke(prompt)

    return response.content.strip().lower()
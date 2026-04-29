# backend/agent/multi_step.py

from tools.rag_tool import rag_tool
from tools.web_search_tool import web_search_tool
from tools.calculator_tool import calculator_tool
from tools.llm_tool import llm_tool
import re


def is_multi_step_query(query):
    """
    Detect if query requires multiple steps
    """

    keywords = [
        "compare",
        "difference",
        "convert",
        "total",
        "sum",
        "analyze"
    ]

    query_lower = query.lower()

    return any(bool(re.search(rf"\b{word}\b", query_lower)) for word in keywords)


def multi_step_pipeline(query, chat_history=None):
    """
    Handle complex queries using multiple tools (multi-step reasoning)
    """

    query_lower = query.lower()

    # CASE 1: COMPARE / DIFFERENCE
    if re.search(r"\bcompare\b|\bdifference\b", query_lower):

        # Step 1 → RAG
        rag_result = rag_tool(query)

        # Step 2 → Web
        web_result = web_search_tool(query)

        # Step 3 → LLM combine
        combined_prompt = f"""
        Compare the following:

        Document Info:
        {rag_result.get('answer', '')}

        Latest Info:
        {web_result.get('answer', '')}

        Give a clear and structured comparison.
        """

        final = llm_tool(combined_prompt)

        return {
            "tool": "multi_step_compare",
            "answer": final.get("answer")
        }

    # CASE 2: TOTAL / SUM
    elif re.search(r"\btotal\b|\bsum\b", query_lower):

        # Step 1 → RAG
        rag_result = rag_tool(query)

        # Step 2 → Extract numbers using LLM
        extract_prompt = f"""
        Extract all numbers from the text below and return only numbers separated by +:

        {rag_result.get('answer', '')}

        Example output:
        10 + 20 + 30
        """

        numbers_expression = llm_tool(extract_prompt).get("answer")

        # Step 3 → Calculator
        calc_result = calculator_tool(numbers_expression)

        return {
            "tool": "multi_step_total",
            "answer": calc_result.get("answer")
        }

    # CASE 3: CONVERT
    elif re.search(r"\bconvert\b", query_lower):

        # Step 1 → Web (get conversion info)
        web_result = web_search_tool(query)

        # Step 2 → LLM (final conversion explanation)
        final_prompt = f"""
        Based on the following data, perform the conversion:

        {web_result.get('answer', '')}

        Question:
        {query}
        """

        final = llm_tool(final_prompt)

        return {
            "tool": "multi_step_convert",
            "answer": final.get("answer")
        }

    # CASE 4: ANALYZE
    elif re.search(r"\banalyze\b", query_lower):

        # Step 1 → RAG
        rag_result = rag_tool(query)

        # Step 2 → LLM analysis
        analysis_prompt = f"""
        Analyze the following content in detail:

        {rag_result.get('answer', '')}
        """

        final = llm_tool(analysis_prompt)

        return {
            "tool": "multi_step_analyze",
            "answer": final.get("answer")
        }

    # DEFAULT FALLBACK
    else:
        final = llm_tool(query)

        return {
            "tool": "multi_step_default",
            "answer": final.get("answer")
        }
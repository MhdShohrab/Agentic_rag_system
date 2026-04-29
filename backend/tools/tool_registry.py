# main file of this folder
# backend/tools/tool_registry.py
from tools.rag_tool import rag_tool
from tools.calculator_tool import calculator_tool
from tools.llm_tool import llm_tool
from tools.summarizer_tool import summarizer_tool
from tools.web_search_tool import web_search_tool

# MCP Core
#CENTRAL TOOL REGISTRY
TOOLS = {
    "rag": rag_tool,
    "calculator": calculator_tool,
    "llm": llm_tool,
    "summarizer": summarizer_tool,
    "web": web_search_tool
}


def get_tool(tool_name):
    """
    Returns the tool function based on tool name
    """
    return TOOLS.get(tool_name)


def list_tools():
    """
    Returns all available tools
    """
    return list(TOOLS.keys())
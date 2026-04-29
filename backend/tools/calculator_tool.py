from dotenv import load_dotenv
import os

load_dotenv()

# upr wala code testing ka h.
def calculator_tool(query, chat_history=None):
    """
    Simple calculator tool
    Handles math expressions
    """

    try:
        result = eval(query)     #Python's built-in eval() fn to evaluate mathematical exp.

        return {
            "tool": "calculator",
            "answer": str(result)
        }

    except Exception as e:
        return {
            "tool": "calculator",
            "answer": f"Error: {str(e)}"
        }
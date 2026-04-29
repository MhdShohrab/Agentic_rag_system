# backend/agent/executor.py
# this file call the tool

from tools.tool_registry import get_tool

def execute_tool(tool_name, query, chat_history=None):
    """
    Execution Layer:
    - Validate tool
    - Execute tool
    - Format output
    - Handle errors
    """

    # print(f"[Executor] Requested Tool: {tool_name}")

    # Step 1: Validate tool
    tool = get_tool(tool_name)

    if not tool:
        return {
            "tool": "error",
            "answer": f"Tool '{tool_name}' not found"
        }

    try:
        # Step 2: Execute tool
        result = tool(query, chat_history)

        # Step 3: Validate response format
        if not isinstance(result, dict):
            return {
                "tool": tool_name,
                "answer": "Invalid response format from tool"
            }

        # 🔹 Step 4: Ensure required keys
        if "answer" not in result:
            result["answer"] = "No answer returned"

        if "tool" not in result:
            result["tool"] = tool_name

        print(f"[Executor] Tool '{tool_name}' executed successfully")

        return result

    except Exception as e:
        return {
            "tool": tool_name,
            "answer": f"Execution Error: {str(e)}"
        }
# main file of this folder.
# backend/agent/agent_pipeline.py
# brain flow 

from agent.decision import decide_tool
from agent.executor import execute_tool
from agent.multi_step import is_multi_step_query, multi_step_pipeline
from memory.memory_manager import (
    add_user_message,
    add_ai_message,
    get_formatted_history
)

def agent_pipeline(query, user_id="default_user"):
    """
    Full Agent Pipeline:
    - Detect multi-step
    - Agent with memory
    - Return structured response
    """

    # Memory
    #Step 1: Load chat history
    chat_history = get_formatted_history(user_id)

    #Step 2: Save user message
    add_user_message(user_id, query)

    # CHECK MULTI-STEP
    if is_multi_step_query(query):

        result = multi_step_pipeline(query, chat_history)

        answer = result.get("answer")       #upr wala result
        # Save AI response
        add_ai_message(user_id, answer)     #saving in the memory

        return {
            "query": query,
            "type": "multi_step",
            "tool_used": result.get("tool"),
            "answer": answer
        }

    # SINGLE-STEP FLOW
    tool_name = decide_tool(query, chat_history)

    result = execute_tool(tool_name, query, chat_history)
    answer = result.get("answer")

    # Save AI response
    add_ai_message(user_id, answer)       #memory
    return {
        "query": query,
        "type": "single_step",
        "tool_used": tool_name,
        "answer": answer
    }
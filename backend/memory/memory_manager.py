# main file of this folder
# backend/memory/memory_manager.py
from memory.memory_store import get_memory, save_memory
from tools.llm_tool import llm_tool

# CONFIG
MAX_RECENT = 6   # last 6 messages (3 user + 3 assistant)


# INITIALIZE MEMORY STRUCTURE
def _init_memory(user_id):
    memory = get_memory(user_id)

    # Convert old format → new format if needed
    if isinstance(memory, list):
        memory = {
            "summary": "",
            "recent": memory
        }

    if "summary" not in memory:
        memory["summary"] = ""

    if "recent" not in memory:
        memory["recent"] = []

    # Removed redundant save_memory call here to optimize performance.
    # save_memory(user_id, memory)
    return memory


# LOAD MEMORY
def load_chat_history(user_id):
    return _init_memory(user_id)


# ADD USER MESSAGE
def add_user_message(user_id, query):
    memory = _init_memory(user_id)

    memory["recent"].append({
        "role": "user",
        "content": query
    })

    _handle_memory_limit(user_id, memory)


# ADD AI MESSAGE
def add_ai_message(user_id, response):
    memory = _init_memory(user_id)

    memory["recent"].append({
        "role": "assistant",
        "content": response
    })

    _handle_memory_limit(user_id, memory)


# HANDLE MEMORY LIMIT (HYBRID) #_handle_memory_limit() = FINAL STEP of memory update
def _handle_memory_limit(user_id, memory):

    if len(memory["recent"]) > MAX_RECENT:

        # Split old + recent
        old_msgs = memory["recent"][:-MAX_RECENT]

        # Summarize old messages
        summary_text = summarize_messages(old_msgs)

        # Append to summary
        if memory["summary"]:
            memory["summary"] += "\n" + summary_text
        else:
            memory["summary"] = summary_text

        # Keep only latest messages
        memory["recent"] = memory["recent"][-MAX_RECENT:]
    # SINGLE SAVE POINT
    save_memory(user_id, memory)

# SUMMARIZATION FUNCTION
def summarize_messages(messages):
    text = "\n".join([
        f"{m['role']}: {m['content']}" for m in messages
    ])

    prompt = f"""
    Summarize the following conversation briefly and clearly:

    {text}
    """

    result = llm_tool(prompt)

    return result.get("answer", "")


# FORMAT HISTORY FOR LLM
def get_formatted_history(user_id):
    memory = _init_memory(user_id)

    summary = memory.get("summary", "")
    recent = memory.get("recent", [])

    formatted = ""

    # Add summary (long-term memory)
    if summary:
        formatted += f"Summary:\n{summary}\n\n"

    # Add recent (short-term memory)
    formatted += "Recent Conversation:\n"

    for msg in recent:
        formatted += f"{msg['role']}: {msg['content']}\n"

    return formatted




# # memory/memory_manager.py
# from langchain.memory import ConversationBufferMemory

# def get_memory():
#     """
#     Creates and returns conversation memory
#     """
#     memory = ConversationBufferMemory(
#         memory_key="chat_history",   # must match prompt
#         return_messages=True         # keeps full conversation
#     )
#     return memory
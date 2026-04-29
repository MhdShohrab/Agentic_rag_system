# backend/memory/memory_schema.py

def create_message(role, content):
    """
    Create a structured message
    role: 'user' or 'assistant'
    """
    return {
        "role": role,
        "content": content
    }
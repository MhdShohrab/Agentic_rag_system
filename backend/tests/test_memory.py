# backend/tests/test_agent.py
# this test case is not just for memory
from agent.agent_pipeline import agent_pipeline
from tools.tool_registry import list_tools
from memory.memory_store import get_memory

def run_tests():

    user_id = "test_user"

    print("\n.............................")
    print("AVAILABLE TOOLS")
    print(list_tools())

    print("\n.............................")
    print("STARTING TESTS")

    queries = [
        # Calculator (Priority 1)
        "25 * 40",

        # Web (Priority 2)
        "latest AI news",

        # RAG (Priority 3)
        "Explain this pdf document",

        # LLM fallback
        "What is Artificial Intelligence?",

        # Multi-step queries
        "Compare document with latest AI trends",
        "Find total cost from document",
        # "Convert 100 USD to INR",
        # "Analyze the document",

        # # Memory test (follow-up)
        # "Who is md shohrab?",
        # "Tell me again what you said about shohrab"
    ]

    for i, q in enumerate(queries, 1):

        print("\n.............................")
        print(f"TEST CASE {i}")

        result = agent_pipeline(q, user_id=user_id)

        print(f"Query       : {result['query']}")
        print(f"Type        : {result['type']}")
        print(f"Tool Used   : {result['tool_used']}")
        print(f"Answer      : {result['answer']}")

    print("\n.................................")
    print("ALL TESTS COMPLETED")
    
    # to print the store data of memory.json in the terminal.     
    # print("\n CURRENT MEMORY:")
    # print(get_memory("test_user"))

if __name__ == "__main__":
    run_tests()
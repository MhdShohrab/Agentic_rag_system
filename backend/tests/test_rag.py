# backend/tests/test_rag_tool.py

from tools.rag_tool import rag_tool

query = "What is AI?"

result = rag_tool(query)

print(f"Query: {query}\nAnswer: {result['answer']}")   # as json is coming then its answer part is only printing.
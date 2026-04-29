from tools.calculator_tool import calculator_tool
from tools.llm_tool import llm_tool
from tools.summarizer_tool import summarizer_tool
from tools.web_search_tool import web_search_tool

print(calculator_tool("25 * 40"))
print(llm_tool("What is AI?"))
print(summarizer_tool("Explain the document"))
print(web_search_tool("Latest AI news"))
from langchain_groq import ChatGroq

def generate_response(query, docs):
    context = "\n\n".join([doc.page_content for doc in docs])

    llm = ChatGroq(
        model_name="llama-3.1-8b-instant",
        temperature=0.3
    )

    prompt = f"""
    You are a helpful assistant.

    Answer ONLY from the context below.
    If answer is not present, say "I don't know".

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.invoke(prompt)
    return response.content


# from langchain.prompts import PromptTemplate

# def get_prompt():
#     """
#     Defines how chatbot behaves
#     """
#     prompt = PromptTemplate(
#         input_variables=["chat_history", "input"],

#         template="""
# You are a helpful AI assistant.

# Use the previous conversation to understand context.
# Answer clearly and correctly.

# Chat History:
# {chat_history}

# User: {input}
# AI:
# """
#     )

#     return prompt
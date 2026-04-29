from langchain_community.vectorstores import FAISS
# file import
from rag.embeddings import get_embeddings

def create_vector_db(chunks):
    embeddings = get_embeddings()
    return FAISS.from_documents(chunks, embeddings)

# Save Vector DB
def save_vector_db(vector_db):
    vector_db.save_local("vectorstore")

# Load Vector DB
def load_vector_db():
    embeddings = get_embeddings()
    return FAISS.load_local(
        "vectorstore",         #local folder where embedded file.
        embeddings,
        allow_dangerous_deserialization=True      #security parameter required by the library (LangChain).
    )

# The load_vector_db function is responsible for loading 
# your existing knowledge base (the vectors created from 
# your PDFs) from your computer's storage into 
# the application's memory so it can be searched.
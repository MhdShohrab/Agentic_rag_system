# this is the main file of this folder
from rag.loader import load_pdf
from rag.splitter import chunk_documents
from rag.vectorstore import create_vector_db, save_vector_db, load_vector_db
from rag.retriever import retrieve_docs
from rag.generator import generate_response

# dynamic way se UI se file upload hoga, build_vector_db(file_path), if you want to test before UI building then use tests folder for it.
def build_vector_db(file_path):
    docs = load_pdf(file_path)
    chunks = chunk_documents(docs)
    vector_db = create_vector_db(chunks)
    save_vector_db(vector_db)
    return vector_db

def build_vector_db_multiple(file_paths):
    """
    Build vector DB from multiple PDFs (1–3)
    """

    all_docs = []

    # 🔹 Step 1: Load all PDFs
    for path in file_paths:
        docs = load_pdf(path)
        all_docs.extend(docs)

    # 🔹 Step 2: Chunk all documents together
    chunks = chunk_documents(all_docs)

    # 🔹 Step 3: Create vector DB
    vector_db = create_vector_db(chunks)

    # 🔹 Step 4: Save DB
    save_vector_db(vector_db)

    return vector_db

def rag_query(query):
    vector_db = load_vector_db()
    docs = retrieve_docs(vector_db, query)
    answer = generate_response(query, docs)
    return answer
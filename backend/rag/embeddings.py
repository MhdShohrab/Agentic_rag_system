# Embedding(hugging face) 
from langchain_community.embeddings import HuggingFaceEmbeddings

# Initialize hugging embeddings
def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

# 1. Separation of Concerns
# embeddings.py → only embeddings
# vectorstore.py → only DB

# 2. Reusability

# Now we can use embeddings anywhere
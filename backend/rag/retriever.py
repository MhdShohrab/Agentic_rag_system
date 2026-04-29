def retrieve_docs(vector_db, query, k=3):
    return vector_db.similarity_search(query, k=k)

# When vector_db.similarity_search(query) is called, the 
# vector store (FAISS) automatically takes the query 
# string and uses its internal embedding function to 
# turn it into a vector before performing the search.
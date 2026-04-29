
# to split into chunks
from langchain_text_splitters import RecursiveCharacterTextSplitter

# making Chunks of the pdf
def chunk_documents(documents):
    """
    This function splits documents into smaller chunks
    """

    # Initialize text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,      # size of each chunk
        chunk_overlap=50     # overlap between chunks
    )

    # Split documents into chunks
    chunks = text_splitter.split_documents(documents)

    return chunks
# LangChain document loader
from langchain_community.document_loaders import PyPDFLoader

# Load whole pdf
def load_pdf(file_path):
    
    # This function loads a PDF and extracts text using LangChain

    try:
        # Initialize PDF loader
        loader = PyPDFLoader(file_path)

        # Load document (returns list of pages)
        documents = loader.load()

        return documents

    except Exception as e:
        print(f"Error loading PDF: {e}")
        return None
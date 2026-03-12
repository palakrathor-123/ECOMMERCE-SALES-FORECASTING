from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def create_vector_db():
    # 1. CSV Loader use karke data load karein
    loader = CSVLoader(file_path='../data/sales_data.csv')
    documents = loader.load()

    # 2. Embedding Model setup (HuggingFace)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 3. Vector Database (Chroma) mein store karein
    vector_db = Chroma.from_documents(
        documents=documents, 
        embedding=embeddings, 
        persist_directory="../data/ecommerce_db"
    )
    print("✅ Embedding Complete: CSV data vector database mein convert ho gaya.")

if _name_ == "_main_":
    create_vector_db()
from dotenv import load_dotenv
import os
from pathlib import Path
from src.helper import load_pdf_files, filter_minimal_docs, create_chunks_from_documents, download_embedding
from pinecone import Pinecone
from pinecone import ServerlessSpec 
from langchain_pinecone import PineconeVectorStore
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings

load_dotenv()

PINECONE_API_KEY= os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

data_dir = Path.home() / "Desktop/medical-chatbot/medical-chatbot/data"
extracted_data = load_pdf_files(str(data_dir))
filter_data = filter_minimal_docs(extracted_data)
text_chunks = create_chunks_from_documents(filter_data)

embeddings = download_embedding()

pinecone_api_key  = PINECONE_API_KEY
pc = Pinecone(api_key=pinecone_api_key)

index_name = "medical-chatbot"  # change if desired

if not pc.has_index(index_name):
    pc.create_index(
        name = index_name,
        dimension=384,
        metric = "cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
index = pc.Index(index_name)

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    embedding=embeddings,
    index_name=index_name
)
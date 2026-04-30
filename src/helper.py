from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from typing import List
import re


def load_pdf_files(data):
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    documents = loader.load()
    return documents


def filter_minimal_docs(docs: List[Document]) -> List[Document]:
    minimal_docs: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src}
            )
        )
    return minimal_docs


def clean_text(text):
    text = re.sub(r"-\n", "", text)
    text = re.sub(r"\n+", "\n", text)
    return text.strip()


def is_useful(text):
    noise = ["introduction", "appendix", "index", "preface", "contents"]
    return text and not any(word in text.lower() for word in noise)


def create_chunks_from_documents(documents, chunk_size=500, chunk_overlap=20):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = []
    for doc in documents:
        content = clean_text(doc.page_content)
        if not is_useful(content):
            continue
        splits = splitter.split_text(content)
        for chunk in splits:
            chunks.append(Document(
                page_content=chunk,
                metadata={
                    "source": doc.metadata.get("source", "unknown"),
                    "page": doc.metadata.get("page", 0),
                }
            ))
    return chunks


def download_embedding():
    return OpenAIEmbeddings(model="text-embedding-ada-002")
import os

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


DATA_PATH = "data/raw_docs"
CHROMA_PATH = "data/chroma"


def load_documents():
    docs = []

    if not os.path.exists(DATA_PATH):
        print("No data folder found")
        return docs

    for file in os.listdir(DATA_PATH):
        path = os.path.join(DATA_PATH, file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(path)
            docs.extend(loader.load())

        elif file.endswith(".txt"):
            loader = TextLoader(path)
            docs.extend(loader.load())

    return docs


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    return splitter.split_documents(documents)


def build_vector_db():
    print("Loading documents...")
    documents = load_documents()

    if len(documents) == 0:
        print("No documents found. Add files inside data/raw_docs/")
        return

    print("Splitting documents...")
    chunks = split_documents(documents)

    print("Loading FREE local embedding model...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Building vector DB...")
    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=CHROMA_PATH
    )

    db.persist()
    print("Vector DB created successfully!")


if __name__ == "__main__":
    build_vector_db()


from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


CHROMA_PATH = "data/chroma"


def get_retriever():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings
    )

    return db.as_retriever(search_kwargs={"k": 3})


def query_documents(question):
    retriever = get_retriever()
    docs = retriever.invoke(question)

    print("\nTop Retrieved Chunks:\n")
    for i, doc in enumerate(docs):
        print(f"Chunk {i+1}:")
        print(doc.page_content)
        print("-" * 40)


if __name__ == "__main__":
    question = input("Ask question: ")
    query_documents(question)


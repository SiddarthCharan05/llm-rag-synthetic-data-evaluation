from src.retrieval.query_db import get_retriever


def generate_answer(question):
    retriever = get_retriever()
    docs = retriever.invoke(question)

    if not docs:
        return "I don't have enough information in the documents."

    context = "\n".join([doc.page_content for doc in docs])

    answer = f"""
Based on retrieved documents:

{context}

Answer:
{context}
"""

    return answer


if __name__ == "__main__":
    question = input("Ask question: ")
    result = generate_answer(question)

    print("\nGenerated Answer:\n")
    print(result)


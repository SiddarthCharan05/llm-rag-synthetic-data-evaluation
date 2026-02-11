import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.rag.simple_rag import generate_answer

st.set_page_config(page_title="RAG Assistant", layout="centered")

st.title("📚 RAG Knowledge Assistant")
st.write("Ask questions from your document knowledge base")

question = st.text_input("Ask a question:")

if question:
    answer = generate_answer(question)

    st.subheader("Answer")
    st.write(answer)


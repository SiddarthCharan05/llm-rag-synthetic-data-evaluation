# llm-rag-synthetic-data-evaluation
End-to-end RAG system for reliable LLM responses using document retrieval, synthetic data generation, and automated evaluation. Includes vector search, grounded answer generation with citations, hallucination detection, and synthetic Q&amp;A creation to simulate real-world enterprise LLM data and evaluation workflows.

# 📚 RAG Knowledge Assistant (Local, Cost-Free)

An end-to-end Retrieval Augmented Generation (RAG) system built using local embeddings and vector search.  
This project demonstrates how to build reliable LLM-style applications without paid APIs.

---

## 🚀 Features

- 📄 Document ingestion (PDF / TXT)
- ✂️ Smart text chunking
- 🧠 Local embedding generation (Sentence Transformers)
- 🗄 Vector database (ChromaDB)
- 🔍 Semantic retrieval
- 💬 Context grounded answer generation
- 🌐 Streamlit web interface
- 💰 Fully local — No OpenAI cost

---

## 🖥 Demo

![RAG UI Demo](docs/rag_ui_demo.png)

---

## 🧠 Architecture

User Question  
↓  
Retriever (Vector Search)  
↓  
Relevant Document Chunks  
↓  
Answer Generator (Grounded Response)  

---

## 🛠 Tech Stack

| Component | Tool |
|---|---|
| Language | Python |
| RAG Framework | LangChain |
| Vector DB | ChromaDB |
| Embeddings | Sentence Transformers |
| UI | Streamlit |
| Environment | Python venv |

---

## 📂 Project Structure


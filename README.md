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
src/
├ ingestion/
│ └ build_index.py
├ retrieval/
│ └ query_db.py
├ rag/
│ └ simple_rag.py
app/
└ chat_app.py
data/
├ raw_docs/
└ chroma/
docs/
└ rag_ui_demo.png


---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/llm-rag-synthetic-data-evaluation.git
cd llm-rag-synthetic-data-evaluation

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt


▶️ Run Project
Build Vector Database
python src/ingestion/build_index.py
Launch Web App
python -m streamlit run app/chat_app.py


📚 Example Usage
Ask:
What is RAG?
What does this document say?
🎯 Why This Project
This project was built to demonstrate:
Data-centric AI thinking
LLM grounding to reduce hallucination
Cost-efficient local LLM infrastructure
Production-style pipeline design
🚀 Future Improvements
Synthetic data generation
Evaluation metrics (faithfulness, hallucination detection)
Chat history memory
Cloud deployment
👩‍💻 Author
Charan Siddarth

---

# 🚀 STEP 3 — Push README

```bash
git add README.md
git commit -m "Add professional README documentation"
git push

# ⚖️ AI Legal Document System

An AI-powered **Legal Document Question-Answering System** built using **Retrieval-Augmented Generation (RAG)**. The system processes legal documents, converts them into searchable vector representations, stores them in **ChromaDB**, and uses an **LLM** to generate context-aware answers based on the retrieved information.

---

## 🚀 Key Features

* 📄 **Legal Document Processing** — Processes a collection of legal PDF documents.
* ✂️ **Document Chunking** — Splits large documents into smaller, meaningful chunks for efficient retrieval.
* 🧠 **Text Embeddings** — Converts document chunks into numerical vector representations.
* 🗄️ **ChromaDB Vector Database** — Stores and retrieves document embeddings using semantic similarity.
* 🔍 **Semantic Search** — Retrieves the most relevant legal document chunks for a user query.
* 🤖 **LLM-powered Answers** — Generates responses using the retrieved legal context.
* 📚 **Context-Grounded Responses** — Answers are generated based on information retrieved from the legal knowledge base.

---

## 🧠 RAG Architecture

The project follows this Retrieval-Augmented Generation pipeline:

```text
                Legal PDF Documents
                        │
                        ▼
              ┌──────────────────┐
              │ Text Extraction  │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │    Chunking      │
              │ Split Documents  │
              │  into Chunks     │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │   Embeddings     │
              │ Text → Vectors   │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │    ChromaDB      │
              │ Vector Database  │
              └────────┬─────────┘
                       │
                       │
User Query ────────────┤
                       ▼
              ┌──────────────────┐
              │ Semantic Search  │
              │ Relevant Chunks  │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │      LLM         │
              │ Answer Generation│
              └────────┬─────────┘
                       │
                       ▼
                  Final Answer
```

---

## 🔄 How It Works

### 1. Document Loading

Legal PDF documents are loaded into the system and their text is extracted.

### 2. Chunking

Large documents are divided into smaller text chunks. This makes the information easier to search and allows the retrieval system to work with focused pieces of content.

### 3. Embedding Generation

Each chunk is converted into a vector representation using an embedding model.

```text
Legal Text → Embedding Model → Vector Representation
```

### 4. ChromaDB Storage

The generated embeddings are stored in **ChromaDB**, which acts as the vector database.

```text
Document Chunk
      ↓
Embedding
      ↓
ChromaDB
```

### 5. Query Retrieval

When a user asks a question, the query is also converted into an embedding. ChromaDB performs similarity search and retrieves the most relevant document chunks.

### 6. LLM Response Generation

The retrieved chunks are provided as context to the **Large Language Model (LLM)**, which generates the final answer.

```text
User Question
      ↓
Query Embedding
      ↓
ChromaDB Similarity Search
      ↓
Relevant Legal Context
      ↓
LLM
      ↓
Final Response
```

---

## 🛠️ Tech Stack

| Technology         | Purpose                                               |
| ------------------ | ----------------------------------------------------- |
| **Python**         | Core programming language                             |
| **RAG**            | Retrieval-Augmented Generation architecture           |
| **Embeddings**     | Converts text into vector representations             |
| **ChromaDB**       | Vector database for storing and retrieving embeddings |
| **LLM**            | Generates answers from retrieved context              |
| **PDF Processing** | Extracts text from legal documents                    |

---

## 📂 Project Structure

```text
AI-Legal-Document-System/
│
├── data/
│   └── Tata_Legal_Knowledge_Base_Complete_30_PDFs/
│       └── Legal PDF Documents
│
├── rag/
│   ├── Embedding
│   ├── Chunking
│   ├── ChromaDB
│   └── LLM / RAG Pipeline
│
├── .gitignore
├── .gitattributes
└── README.md
```

---

## 🎯 Problem Statement

Legal documents can be lengthy and difficult to search manually. Finding relevant information across multiple documents can be time-consuming.

This project provides an AI-powered solution where users can ask questions in natural language and retrieve relevant information from a legal document knowledge base.

---

## 💡 Why RAG?

A normal LLM may not have access to the specific information contained in a user's private document collection.

RAG solves this by connecting the LLM with an external knowledge base:

**Retrieve → Provide Context → Generate Answer**

This allows the LLM to generate responses using relevant information from the indexed legal documents instead of relying only on its pretrained knowledge.

---

## 📚 Knowledge Base

The project uses a collection of **30 Tata legal PDF documents** as the knowledge base.

The documents are processed through the RAG pipeline and converted into searchable vector representations.

---

## 🔮 Future Improvements

* 🌐 Build a user-friendly web interface.
* 📤 Add support for uploading new legal documents.
* 📑 Provide document and page-level citations with answers.
* 🔎 Implement hybrid search and reranking.
* 💬 Add conversational memory for follow-up questions.
* 🚀 Deploy the system as an online legal document assistant.

---

## ⚠️ Disclaimer

This project is intended for **educational and informational purposes only**.

It does not provide professional legal advice. For specific legal matters, users should consult a qualified legal professional.

---

## 👩‍💻 Author

**Jyoti Yadav**

GitHub: **Jyotiyadav010**

⭐ If you find this project useful, consider giving it a star!

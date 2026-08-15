import os

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings
from langchain_groq import ChatGroq
# Load environment variables
load_dotenv()


# Same embedding model used while creating ChromaDB
model = SentenceTransformer("all-MiniLM-L6-v2")


# LangChain wrapper for Sentence Transformers
class SentenceTransformerEmbeddings(Embeddings):

    def embed_documents(self, texts):
        return model.encode(texts).tolist()

    def embed_query(self, text):
        return model.encode(text).tolist()


embedding_function = SentenceTransformerEmbeddings()


# Connect to our existing ChromaDB
vector_store = Chroma(
    collection_name="tata_legal_knowledge",
    embedding_function=embedding_function,
    persist_directory="./chroma_db"
)
# Create retriever
retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)

# Connect to Groq LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# User question
question = "What is the approved liability position?"


# Retrieve relevant chunks
results = retriever.invoke(question)


# Combine retrieved chunks into one context
context = "\n\n".join(
    document.page_content
    for document in results
)


print("Retrieved context:")
print(context)

prompt = f"""
You are a legal document assistant.

Answer the question using ONLY the provided context.
If the answer is not present in the context, say that the information is not available in the provided knowledge base.

Context:
{context}

Question:
{question}

Answer:
"""


response = llm.invoke(prompt)


print("\nFinal Answer:")
print(response.content)



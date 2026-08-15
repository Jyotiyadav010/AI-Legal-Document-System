from sentence_transformers import SentenceTransformer

from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings


# 1. Load the same embedding model

model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Create LangChain embedding wrapper

class SentenceTransformerEmbeddings(Embeddings):

    def embed_documents(self, texts):
        return model.encode(texts).tolist()

    def embed_query(self, text):
        return model.encode(text).tolist()


embedding_function = SentenceTransformerEmbeddings()


# 3. Connect to existing ChromaDB

vector_store = Chroma(
    collection_name="tata_legal_knowledge",
    embedding_function=embedding_function,
    persist_directory="./chroma_db"
)


# 4. Create retriever

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)


# 5. Ask a question

question = "What is the approved liability position?"


# 6. Retrieve relevant chunks

results = retriever.invoke(question)


print("Number of results:", len(results))

for i, document in enumerate(results, start=1):

    print(f"\n--- Result {i} ---")
    print("Source:", document.metadata.get("source"))
    print("Page:", document.metadata.get("page"))
    print("Content:")
    print(document.page_content)
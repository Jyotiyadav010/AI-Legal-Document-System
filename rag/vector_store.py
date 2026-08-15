from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings



# 1. Knowledge Base path


DATA_PATH = Path("data/Tata_Legal_Knowledge_Base_Complete_30_PDFs")



# 2. Load PDFs


pdf_files = list(DATA_PATH.rglob("*.pdf"))

documents = []

for pdf_file in pdf_files:
    loader = PyPDFLoader(str(pdf_file))
    pages = loader.load()
    documents.extend(pages)

print("Total PDFs:", len(pdf_files))
print("Total pages:", len(documents))


# 3. Create chunks

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print("Total chunks:", len(chunks))


# 4. Load embedding model

model = SentenceTransformer("all-MiniLM-L6-v2")



# 5. Create LangChain Embeddings wrapper

class SentenceTransformerEmbeddings(Embeddings):

    def embed_documents(self, texts):
        return model.encode(texts).tolist()

    def embed_query(self, text):
        return model.encode(text).tolist()


embedding_function = SentenceTransformerEmbeddings()


# 6. Store in ChromaDB

vector_store = Chroma(
    collection_name="tata_legal_knowledge",
    embedding_function=embedding_function,
    persist_directory="./chroma_db"
)

vector_store.add_documents(chunks)

print("Documents successfully stored in ChromaDB!")
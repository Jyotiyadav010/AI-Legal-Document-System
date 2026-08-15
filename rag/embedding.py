from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer


# 1. Knowledge Base folder
DATA_PATH = Path("data/Tata_Legal_Knowledge_Base_Complete_30_PDFs")


# 2. Find all PDFs
pdf_files = list(DATA_PATH.rglob("*.pdf"))

print("Total PDF files found:", len(pdf_files))


# 3. Load PDF pages
documents = []

for pdf_file in pdf_files:
    loader = PyPDFLoader(str(pdf_file))
    pages = loader.load()
    documents.extend(pages)

print("Total pages loaded:", len(documents))


# 4. Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print("Total chunks created:", len(chunks))


# 5. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 6. Extract text from every chunk
texts = [chunk.page_content for chunk in chunks]


# 7. Create embeddings
embeddings = model.encode(texts)

print("Total embeddings created:", len(embeddings))
print("Embedding dimensions:", embeddings.shape[1])
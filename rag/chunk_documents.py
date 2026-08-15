from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Knowledge Base folder
DATA_PATH = Path("data/Tata_Legal_Knowledge_Base_Complete_30_PDFs")


# 1. Find all PDF files
pdf_files = list(DATA_PATH.rglob("*.pdf"))

print("Total PDF files found:", len(pdf_files))


# 2. Load all PDF pages
documents = []

for pdf_file in pdf_files:
    loader = PyPDFLoader(str(pdf_file))
    pages = loader.load()
    documents.extend(pages)


print("Total pages loaded:", len(documents))


# 3. Create text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)


# 4. Split documents into chunks
chunks = text_splitter.split_documents(documents)


print("Total chunks created:", len(chunks))
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


# Knowledge Base ka folder
DATA_PATH = Path("data/Tata_Legal_Knowledge_Base_Complete_30_PDFs")


documents = []

# Saare subfolders ke andar PDF files dhundho
pdf_files = list(DATA_PATH.rglob("*.pdf"))

print("Total PDF files found:", len(pdf_files))


# Har PDF ko load karo
for pdf_file in pdf_files:
    loader = PyPDFLoader(str(pdf_file))
    pages = loader.load()
    documents.extend(pages)


print("Total pages loaded:", len(documents))
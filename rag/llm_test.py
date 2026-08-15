import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq


# Load variables from .env
load_dotenv()
print("API key loaded:", bool(os.getenv("GROQ_API_KEY")))


# Connect to Groq
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)


# Simple test
response = llm.invoke("Explain what a legal contract is in one sentence.")

print(response.content)
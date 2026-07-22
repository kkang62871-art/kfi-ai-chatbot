import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()
import os

print(os.getenv("OPENAI_API_KEY"))
# OpenAI Embedding 모델
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# PDF 폴더
PDF_FOLDER = "pdf"

documents = []

for file in os.listdir(PDF_FOLDER):

    if file.endswith(".pdf"):

        loader = PyPDFLoader(os.path.join(PDF_FOLDER, file))

        docs = loader.load()

        for doc in docs:
            doc.metadata["file"] = file

        documents.extend(docs)

print(f"불러온 페이지 수 : {len(documents)}")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

chunks = splitter.split_documents(documents)

print(f"Chunk 개수 : {len(chunks)}")

Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)

print("ChromaDB 저장 완료!")
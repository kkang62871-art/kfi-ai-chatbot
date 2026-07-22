from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

def search_context(question):

    docs = db.similarity_search(question, k=3)

    print("검색 결과 개수:", len(docs))

    for i, doc in enumerate(docs):
        print(f"\n===== 문서 {i+1} =====")
        print(doc.metadata)
        print(doc.page_content[:300])

    context = ""

    for doc in docs:
        context += f"""
파일 : {doc.metadata.get("file")}

페이지 : {doc.metadata.get("page")}

내용 :
{doc.page_content}

-----------------------------
"""

    return context
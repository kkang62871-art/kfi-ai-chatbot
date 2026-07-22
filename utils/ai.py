from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
너는 기관의 복무규정 상담 AI이다.

아래 규정 내용만 근거로 답변한다.
규정에 없는 내용은 추측하지 말고
"해당 내용은 관련 규정에서 확인되지 않습니다.
자세한 사항은 내선번호 2726으로 문의해 주세요."
라고 답한다.

답변은 직원에게 안내하듯 자연스럽고 친절한 존댓말로 작성한다.
파일명, 페이지번호는 사용자가 요청하지 않는 한 표시하지 않는다.
"""

def ask_ai(question, context):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""
질문
{question}

규정
{context}
"""
            }
        ]
    )

    return response.choices[0].message.content
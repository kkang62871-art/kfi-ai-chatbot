import streamlit as st
from utils.rag import search_context
from utils.ai import ask_ai

st.set_page_config(
    page_title="복무 상담원 AI",
    page_icon="🤖",
    layout="centered"
)

# CSS 불러오기
with open("style.css", "r", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# -----------------------------
# Header
# -----------------------------
try:
    st.image("assets/logo.jpg", width=320)
except:
    st.markdown(
        "<h2 style='text-align:center'>🤖</h2>",
        unsafe_allow_html=True
    )

st.markdown(
    """
<h1 class="title">
복무 상담원 AI
</h1>

<p class="subtitle">
복무규정 · 복무규칙 · 여비규칙을 AI가 빠르게 찾아드립니다.
</p>
""",
    unsafe_allow_html=True
)

# -----------------------------
# 세션
# -----------------------------
if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role":"assistant",
            "content":
"""
안녕하세요 😊

궁금한 내용을 입력하면 관련 규정을 찾아
쉽게 설명해드립니다.

예시)

• 병가는 며칠 사용할 수 있나요?

• 출장 여비는 어떻게 지급되나요?

• 특별휴가는 언제 사용할 수 있나요?
"""
        }
    ]

# -----------------------------
# 대화 출력
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# -----------------------------
# 질문 입력
# -----------------------------
question = st.chat_input(
    "궁금한 내용을 입력하세요."
)

# -----------------------------
# 질문 처리
# -----------------------------
if question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("관련 규정을 검색하고 있습니다..."):

            context = search_context(question)

            answer = ask_ai(
                question,
                context
            )

        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )
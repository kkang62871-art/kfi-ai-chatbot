# app.py
import streamlit as st
from utils.rag import search_context
from utils.ai import ask_ai

st.set_page_config(
    page_title="복무 상담원 AI",
    page_icon="🤖",
    layout="centered"
)

with open("style.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown('<div class="header">🤖 복무 상담원 AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">복무 관련 규정을 쉽고 빠르게 안내해드립니다.</div>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role":"assistant","content":"안녕하세요. 복무 관련 규정에 대해 궁금한 사항을 질문해 주세요."}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.chat_input("질문을 입력하세요.")

if question:
    st.session_state.messages.append({"role":"user","content":question})

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("규정을 검색하는 중입니다..."):
            context = search_context(question)
            answer = ask_ai(question, context)
        st.markdown(answer)

    st.session_state.messages.append(
        {"role":"assistant","content":answer}
    )

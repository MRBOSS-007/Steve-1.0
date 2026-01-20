import streamlit as st
from agent import chat

st.set_page_config(
    page_title="Sri Vishnu Suresh – AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Steve 1.0")
st.caption("Ask me about vishnu's background, skills, experience, or projects.")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Display previous messages
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask a question...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.history.append({
        "role": "user",
        "content": user_input
    })

    # Assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat(user_input, st.session_state.history[:-1])
            st.markdown(response)

    st.session_state.history.append({
        "role": "assistant",
        "content": response
    })

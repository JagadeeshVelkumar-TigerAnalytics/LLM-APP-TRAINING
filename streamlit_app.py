import streamlit as st
from backend.llm_chat_bot import generate_chatbot_response,generate_chatbot_response_without_rag
import requests

st.title("ChatBot")
st.set_page_config(page_title="Chatbot", layout="centered")
new_chat_button = st.sidebar.button(label="New Chat")

# Chat history (stored in session)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Say Something!!")

headers = {
    # "Authorization": "Bearer YOUR_TOKEN",  # if needed
    "Content-Type": "application/json"
}

if user_input:
    st.session_state.chat_history.append(("You",user_input))
    # response = generate_chatbot_response_without_rag(user_input)
    print(user_input)
    response = requests.post(url="http://127.0.0.1:8000/chat",json={"user_input":user_input},headers=headers).json()
    print(response["response"])
    st.session_state.chat_history.append(("Bot",response["response"]))

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}",)

if new_chat_button:
    st.session_state.chat_history = []
    st.rerun()
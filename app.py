# Import Libraries
import streamlit as st
import json
from chatbot_api import create_chat_session, send_message

# File to save chat history
HISTORY_FILE = "chat_history.json"

# Streamlit setup
st.set_page_config(page_title="Gemini ChatBot", page_icon="🤖", layout="centered")
st.title("🤖 Gemini AI Chatbot")
st.write("Ask anything! Chat history is saved locally and in session.")

# Initialize chat session
if "chat" not in st.session_state:
    st.session_state["chat"] = create_chat_session()

# Load chat history
if "messages" not in st.session_state:
    try:
        with open(HISTORY_FILE, "r") as f:
            st.session_state["messages"] = json.load(f)
    except FileNotFoundError:
        st.session_state["messages"] = []

# Function to save chat history
def save_history():
    with open(HISTORY_FILE, "w") as f:
        json.dump(st.session_state["messages"], f)

# Display chat messages
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if user_input := st.chat_input("Type your message..."):
    st.chat_message("user").markdown(user_input)
    st.session_state["messages"].append({"role": "user", "content": user_input})
    save_history() # Save after user message

    try:
        ai_response = send_message(st.session_state["chat"], user_input)
        st.chat_message("assistant").markdown(ai_response)
        st.session_state["messages"].append({"role": "assistant", "content": ai_response})
    except Exception as e:
        st.error(f" ⚠️ Error: {e}")

# Clear chat
if st.button("🧹 Clear Chat"):
    st.session_state["chat"] = create_chat_session()
    st.session_state["messages"] = []
    save_history()
    st.rerun()
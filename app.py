# import libraries
import streamlit as st # building the web interface
from google import genai # Google Gemini SDK to talk to the AI model
from dotenv import load_dotenv # Load API KEY
import os # Access environment variables

# Load API Key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize CLient and Chat Session
if "client" not in st.session_state:
    st.session_state["client"] = genai.Client(api_key=API_KEY)

if "chat" not in st.session_state:
    st.session_state["chat"] = st.session_state["client"].chats.create(model="gemini-2.5-flash")

# Streamlit page config
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 Gemini AI Chatbot")
st.write("Ask anything! Chat history is saved in this session.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
                    
# chat input
if prompt := st.chat_input("Type your message..."):
    st.chat_message("user").markdown(prompt)
    st.session_state["messages"].append({"role": "user", "content": prompt})

    try:
        # send user prompt to Gemini AI
        response_stream = st.session_state["chat"].send_message_stream(prompt) # Sends user message to Gemini AI as a stream
        ai_response = ""
        for chunk in response_stream:
            ai_response += chunk.text
            st.chat_message("assistant").markdown(ai_response) # Display streaming text in the chat UI using

        st.session_state["messages"].append({"role": "assistant", "content": ai_response})

    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# Clear chat history button
if st.button("🧹 Clear Chat"):
    # Recreate chat session but keep the same client
    st.session_state["chat"] = st.session_state["client"].chats.create(model="gemini-2.5-flash")
    st.session_state["messages"] = []
    st.rerun()

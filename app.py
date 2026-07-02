import streamlit as st
import ollama

# Page title
st.set_page_config(page_title="Offline Chatbot", page_icon="🤖")

st.title("🤖 Offline Chatbot Using Ollama")

# User input
query = st.text_input("Enter your query:")

# Generate response when the user enters a query
if query:

    conversation = [
        {
            "role": "system",
            "content": (
                "You are a helpful, concise, and knowledgeable AI assistant. "
                "Answer the user's questions clearly and effectively."
            )
        },
        {
            "role": "user",
            "content": query
        }
    ]

    try:
        with st.spinner("Thinking..."):
            response = ollama.chat(
                model="deepseek-r1:1.5b",
                messages=conversation
            )

        full_response = response["message"]["content"]

        with st.chat_message("assistant"):
            st.markdown(full_response)

    except Exception as e:
        st.error(f"Error: {e}")
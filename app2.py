import streamlit as st
import ollama
#deepseek chat application
st.title('Rohit AI')

# Initialize conversation history in session_state
# (persists across Streamlit reruns, unlike a plain variable)
if "conversation" not in st.session_state:
    st.session_state.conversation = [
        {"role": "system", "content": "You are a helpful and concise assistant. Give answers in a very effective way."}
    ]

# Re-render previous messages on every rerun
for msg in st.session_state.conversation:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# Get new user input
query = st.chat_input('Enter any query')

# Only run the model if the user actually typed something
if query:
    # Show user message immediately
    with st.chat_message("user"):
        st.markdown(query)

    # Add user message to history
    st.session_state.conversation.append({"role": "user", "content": query})

    # Call Ollama with FULL history (gives it memory of the conversation)
    response = ollama.chat(
        model="gemma3:latest",
        messages=st.session_state.conversation
    )
    full_response = response['message']['content']

    # Display and store assistant message
    with st.chat_message("assistant"):
        st.markdown(full_response)

    st.session_state.conversation.append({"role": "assistant", "content": full_response})
import streamlit as st
import ollama

st.title("Deepseek chat application!")
if "conversation" not in st.session_state:
    st.session_state.conversation = [
        {"role": "system", "content": "You are a helpful and concise assistant.Give answers in a very effective way."}
    ]
for msg in st.session_state.conversation:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

query = st.chat_input("Enter your query:")
if query:
    with st.chat_message("user"):
        st.markdown(query)

    st.session_state.conversation.append({"role": "user", "content": query})
    response = ollama.chat(
        model="deepseek-r1:1.5b",
        messages=st.session_state.conversation
    )
    full_response = response["message"]["content"]
    with st.chat_message("assistant"):
        st.markdown(full_response)
        st.session_state.conversation.append({"role": "assistant", "content": full_response})

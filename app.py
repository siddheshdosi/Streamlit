import streamlit as st
import requests

st.set_page_config(page_title="AI Agent Demo", layout="centered")

st.title("🤖 AI Agent Chat Demo")

# simple mock agent - replace with LangChain/React Agent logic
def ask_agent(query):
    return f"Agent response for: {query}"

user_input = st.text_input("Ask something:")
if st.button("Send") and user_input:
    response = ask_agent(user_input)
    st.write("### Response:")
    st.success(response)

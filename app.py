import streamlit as st
import requests

# Hide default Streamlit elements
# hide_st_style = """
#     <style>
#     #MainMenu {visibility: hidden;} /* Hamburger menu */
#     footer {visibility: hidden;}    /* Footer */
#     header {visibility: hidden;}    /* Header */
#     </style>
# """
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}  /* hamburger menu */
    footer {visibility: hidden;}     /* footer */
    header {visibility: hidden;}     /* top header */
    .stAppDeployButton {display:none;}  /* deploy/share button */
    .viewerBadge_container__1QSob {display: none !important;} /* hosted with Streamlit badge */
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

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

import boto3
import streamlit as st

st.subheader('Chatbot with SharePoint Custom Data',divider='rainbow')

if 'chat_history' not in st.session_state:
    st.session_state.chat_history=[]

for message in st.session_state.chat_history:
    with st.chat_history(message['role']):
        st.markdown(message['text'])


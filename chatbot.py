import boto3
import streamlit as st

st.subheader('Chatbot with SharePoint Custom Data',divider='rainbow')

if 'chat_history' not in st.session_state:
    st.session_state.chat_history=[]

for message in st.session_state.chat_history:
    with st.chat_history(message['role']):
        st.markdown(message['text'])

bedrockClinet = boto3.client('bedrock-agent-runtime','us-east-1')

def getAnswers(questions):
    knowledgeBaseResponse = bedrockClinet.retrieve_and_generate(
        input={'text':questions},
        retrieveAndGenerateConfiguration ={
            'knowledgeBaseConfiguration':{
                'knowledgeBaseId':'EOTHLX655R'
                'modelArn':'arn:aws:bedrock:us-east-1::foundation-model/cohere.command-text-v14'
            },
            'type':'KNOWLEDGE_BASE'
        })
    return knowledgeBaseResponse

questions = st.chat_input('Enter your question here..')

if questions :
    with st.chat_message('user'):
        st.markdown(questions)
    st.session_state.chat_history.append({"role":'user','text':questions})

    response = getAnswers(questions)

    answer = response['output']['text']

    
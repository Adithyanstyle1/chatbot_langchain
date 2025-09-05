from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

st.title("Chat with Adithyan")
input_txt = st.text_input("Enter your Quries")

prompt = ChatPromptTemplate.from_messages(
    [("system","Your are an helpful AI Assistance ,nameis Adithyan Chatbot"),
     ("user","user query:{query}")
     
     ]
)


llm = Ollama(model="llama2")
outputparser = StrOutputParser()
chain = prompt|llm|outputparser

if input_txt :
    st.write(chain.invoke({"query":input_txt}))

    
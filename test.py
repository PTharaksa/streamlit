from openai import OpenAI
import streamlit as st
import pandas as pd
import time
import os

client = OpenAI()

st.set_page_config(
    page_title="openai",
    layout='wide',
    initial_sidebar_state='auto',
)

st.header("Caption Generator")
st.write("ไอเดียการเขียนแคปชั่นประกอบโพส")
st.sidebar.header("Caption Generator")
st.sidebar.text_input("Please add your OpenAI API key to continue", key='openai_apikey')

if st.session_state.openai_apikey != "":
    st.success('OpenAI API key provided!', icon='✅') #condition detect the invalid api_key
    st.text_input("ต้องการเขียนแคปชั่นเกี่ยวกับอะไร", key = "chatbot_input")


    openai.api_key = st.session_state.openai_apikey
    prompt = f"Write 5 introductions for a blog post about {st.session_state.chatbot_input} and reason why I should use them"
    
    def call_openai_api():
        try:
            response = client.chat.completions.create(
                engine ="text-davinci-002",
                prompt=prompt,
                temperature=0.5,
                max_tokens=3000
            )
            return response
        except openai.RateLimitError as e:
            print(f"Rate limit exceeded. Waiting before making the next request. Error: {e}")
            time.sleep(60)  # Wait for a minute
            return call_openai_api()

    response = call_openai_api()
    st.text_area("Response:", response.choices[0].text.strip())
else:
    st.warning('Please enter your OpenAI API key!', icon='⚠️')

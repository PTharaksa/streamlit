# from openai import OpenAI
# import streamlit as st
# import pandas as pd
# import time
# import os

# st.set_page_config(
#     page_title="openai",
#     layout='wide',
#     initial_sidebar_state='auto',
# )

# st.header("Caption Generator")
# st.write("ไอเดียการเขียนแคปชั่นประกอบโพส")
# st.sidebar.header("Caption Generator")
# st.sidebar.text_input("Please add your OpenAI API key to continue", key='openai_apikey')

# if st.session_state.openai_apikey != "":
#     st.success('OpenAI API key provided!', icon='✅') #condition detect the invalid api_key
#     st.text_input("ต้องการเขียนแคปชั่นเกี่ยวกับอะไร", key = "chatbot_input")


#     OPENAI_API_KEY = st.session_state.openai_apikey
#     client = OpenAI(api_key = OPENAI_API_KEY)

#     prompt = f"Write 5 introductions for a blog post about {st.session_state.chatbot_input} and reason why I should use them"
    
#     def call_openai_api():
#         try:
#             response = client.chat.completions.create(
#                 engine ="text-davinci-002",
#                 prompt=prompt,
#                 temperature=0.5,
#                 max_tokens=3000
#             )
#             return response
#         except openai.RateLimitError as e:
#             print(f"Rate limit exceeded. Waiting before making the next request. Error: {e}")
#             time.sleep(60)  # Wait for a minute
#             return call_openai_api()

#     response = call_openai_api()
#     st.text_area("Response:", response.choices[0].text.strip())
# else:
#     st.warning('Please enter your OpenAI API key!', icon='⚠️')

import openai
import streamlit as st

# Set up the Streamlit app
st.sidebar.header("API Key Configuration")
api_key = st.sidebar.text_input("Enter your OpenAI API key", key="openai_apikey", type="password")

if api_key:
    st.success("OpenAI API key provided!", icon="✅")
    openai.api_key = api_key  # Assign API key to the OpenAI library
else:
    st.warning("Please provide your OpenAI API key!", icon="⚠️")

caption_topic = st.text_input("What topic would you like a caption for?", key="chatbot_input")

if caption_topic and api_key:
    # Define the prompt
    prompt = f"Write 5 introductions for a blog post about {caption_topic} and reasons why I should use them."

    def call_openai_api():
        try:
            # Call OpenAI API
            response = openai.Completion.create(
                engine="text-davinci-003",  # Updated engine for better results
                prompt=prompt,
                temperature=0.5,
                max_tokens=300,
            )
            return response
        except openai.error.OpenAIError as e:
            st.error(f"Error interacting with OpenAI API: {str(e)}")
            return None

    # Get response and display it
    response = call_openai_api()
    if response:
        st.text_area("Generated Captions:", response.choices[0].text.strip())
else:
    st.info("Please enter a topic to generate captions.")


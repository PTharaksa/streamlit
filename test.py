import openai
import streamlit as st

META_PROMPT = ""

st.sidebar.header("API Key Configuration")
api_key = st.sidebar.text_input("Enter your OpenAI API key", key="openai_apikey", type="password")

if api_key:
    st.success("OpenAI API key provided!", icon="✅")
    openai.api_key = st.session_state.openai_apikey
else:
    st.warning("Please provide your OpenAI API key!", icon="⚠️")

caption_topic = st.text_input("What topic would you like a caption for?", key="chatbot_input")

if caption_topic and api_key:
    prompt = f"Write 5 introductions for a blog post about {caption_topic} and reasons why I should use them."

def call_openai_api(prompt):
    response = openai.ChatCompletion.create(
            model="davinci-002",
            messages=[
                {
                "role": "system",
                "content": META_PROMPT,
                },
                {
                "role": "user",
                "content": "Task, Goal, or Current Prompt:\n" + prompt,
                },
            ],
        )
    return completion.choices[0].message.content
    
    response = call_openai_api()
    if response:
        st.text_area("Generated Captions:", response.choices[0].text.strip())
    else:
        st.info("Please enter a topic to generate captions.", icon='⚠️')


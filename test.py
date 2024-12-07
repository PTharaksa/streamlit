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


def call_openai_api(prompt):
    try:
        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
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
    except Exception as e:
        st.error(f"Error while calling OpenAI API: {e}")
        return None

if caption_topic and api_key:
    prompt = f"Write 5 introductions for a blog post about {caption_topic} and reasons why I should use them."
    response = call_openai_api(prompt)

    
if response:
    st.text_area("Generated Captions:", response, height=200)
else:
    st.info("Please enter a topic to generate captions.", icon='⚠️')


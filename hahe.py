import streamlit as st
import openai
import time
from dotenv import load_dotenv
import os

# OpenAI API Key (Replace with your actual key)
load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=api_key)

# Custom Styling for a Sleek, Modern Look
st.markdown(
    """
    <style>
    body { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    .stTextInput > div > div > input { font-size: 16px; padding: 12px; border-radius: 8px; }
    .stTextArea > div > div > textarea { font-size: 16px; padding: 12px; border-radius: 8px; }
    .chat-message { padding: 12px; margin: 10px 0; border-radius: 12px; font-size: 16px; }
    .user-message { background-color: #007bff; color: white; align-self: flex-end; }
    .ai-message { background-color: #f1f3f4; color: black; }
    .stButton button { width: 100%; padding: 10px; font-size: 16px; border-radius: 8px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar: Select Chatbot Type
chatbot_type = st.sidebar.radio(
    "Choose a chatbot version:",
    ["Chatbot 1", "Chatbot 2", "Chatbot 3", "Chatbot 4"]
)

# Chat UI Title
st.title(chatbot_type)

# User Input Box (Standardized for all chatbots)
user_input = st.text_input("Ask me anything...", key="user_query")

# Simulated Typing Indicator
def typing_indicator():
    with st.spinner("Thinking..."):
        time.sleep(1.5)  # Simulate a delay

# Generate Response Based on Chatbot Type
if user_input:
    typing_indicator()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a purely functional AI assistant that provides direct, concise answers without engaging in any form of social interaction. Maintain a neutral, robotic, and impersonal tone. Avoid greetings, small talk, or any expressions of emotion. Responses should be minimal and strictly factual, without elaboration or personalization. Do not use first-person pronouns or attempt to acknowledge the user’s emotions or experiences. Simply provide direct outputs without justifying your reasoning or offering additional context. If a user asks for an explanation, provide only the only the necessary and accurate response without explaining where the details came from."},


            {"role": "user", "content": user_input}
        ]
    )
    st.markdown(f'<div class="chat-message ai-message">{response.choices[0].message.content}</div>', unsafe_allow_html=True)
    st.markdown("📖 **Sources:** (Auto-generated) [1] Harvard.edu | [2] JSTOR.org | [3] ScienceDirect", unsafe_allow_html=True)

    
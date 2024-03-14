import streamlit as st
from typing import Generator
from groq import Groq

# Assuming Deepgram and other necessary imports are correctly set up
# from deepgram import Deepgram

st.set_page_config(page_icon="💬", layout="wide", page_title="Groq Goes Brrrrrrrr...")

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(f'<span style="font-size: 78px; line-height: 1">{emoji}</span>', unsafe_allow_html=True)

icon("🏎️")

# Sidebar for navigation
with st.sidebar:
    st.title("Navigation")
    page = st.radio("Go to", ["Chat", "Settings", "About"])

# Only show chat application if 'Chat' is selected
if page == "Chat":
    st.subheader("Groq Chat Streamlit App")

    client = Groq(api_key=st.secrets["GROQ_API_KEY"])

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "selected_model" not in st.session_state:
        st.session_state.selected_model = None

    models = {
        "mixtral-8x7b-32768": {"name": "Mixtral-8x7b-Instruct-v0.1", "tokens": 32768, "developer": "Mistral"},
        "llama2-70b-4096": {"name": "LLaMA2-70b-chat", "tokens": 4096, "developer": "Meta"},
        "gemma-7b-it": {"name": "Gemma-7b-it", "tokens": 8192, "developer": "Google"}
    }

    col1, col2 = st.columns(2)

    with col1:
        model_option = st.selectbox(
            "Choose a model:",
            options=list(models.keys()),
            format_func=lambda x: models[x]["name"],
            index=0
        )

    if st.session_state.selected_model != model_option:
        st.session_state.messages = []
        st.session_state.selected_model = model_option

    max_tokens_range = models[model_option]["tokens"]

    with col2:
        max_tokens = st.slider(
            "Max Tokens:",
            min_value=512,
            max_value=max_tokens_range,
            value=min(32768, max_tokens_range),
            step=512
        )

    # This is where the microphone icon and its functionality would be integrated
    st.button("🎙️ Start Voice Input") # Placeholder for actual voice input functionality

    if prompt := st.chat_input("Enter your prompt here..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Placeholder for Groq API interaction and response handling

# Additional pages like 'Settings' and 'About' can be filled with respective content
elif page == "Settings":
    st.title("Settings")
    # Settings content here

elif page == "About":
    st.title("About")
    # About content here

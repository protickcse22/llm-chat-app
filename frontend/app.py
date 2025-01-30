import streamlit as st
import requests
from typing import Dict, List
import time

# Configure backend URL
BACKEND_URL = "http://localhost:8000/api/generate"

# Custom CSS
def load_css():
    with open("static/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize session state
def init_session():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "model" not in st.session_state:
        st.session_state.model = "deepseek-r1:7b"
    if "temperature" not in st.session_state:
        st.session_state.temperature = 0.7
    if "top_p" not in st.session_state:
        st.session_state.top_p = 0.9
    if "max_tokens" not in st.session_state:
        st.session_state.max_tokens = 512

# Display chat messages
def display_chat():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Handle user input
def handle_input():
    if prompt := st.chat_input("Type your message..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Add assistant placeholder
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Get response from backend
            try:
                response = requests.post(
                    BACKEND_URL,
                    json={
                        "prompt": prompt,
                        "model": st.session_state.model,
                        "temperature": st.session_state.temperature,
                        "top_p": st.session_state.top_p,
                        "max_tokens": st.session_state.max_tokens,
                    }
                )
                response.raise_for_status()
                full_response = response.json()["response"]
            except Exception as e:
                full_response = f"Error: {str(e)}"
            
            # Simulate streaming
            for chunk in full_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        
        # Add assistant message
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# Main function
def main():
    st.set_page_config(
        page_title="Local LLM Chat",
        page_icon="🤖",
        layout="centered"
    )
    load_css()
    init_session()
    
    # Sidebar
    with st.sidebar:
        st.title("Settings")
        
        # Model selection
        st.session_state.model = st.selectbox(
            "Select Model",
            ["deepseek-r1:7b", "llama2", "mistral"],
            index=0
        )
        
        # Temperature slider
        st.session_state.temperature = st.slider(
            "Temperature",
            min_value=0.1,
            max_value=1.0,
            value=0.7,
            step=0.1,
            help="Controls randomness. Lower values make the output more deterministic."
        )
        
        # Top-p slider
        st.session_state.top_p = st.slider(
            "Top-p",
            min_value=0.1,
            max_value=1.0,
            value=0.9,
            step=0.1,
            help="Controls diversity via nucleus sampling. Lower values mean fewer options."
        )
        
        # Max tokens slider
        st.session_state.max_tokens = st.slider(
            "Max Tokens",
            min_value=64,
            max_value=1024,
            value=512,
            step=64,
            help="Controls the maximum length of the response."
        )
        
        st.markdown("---")
        st.markdown("Powered by Ollama")
    
    # Main chat interface
    st.title("💬 Local LLM Chat")
    display_chat()
    handle_input()

if __name__ == "__main__":
    main()
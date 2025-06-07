import streamlit as st
import requests
import json
from typing import List, Dict

# Configure Streamlit page
st.set_page_config(page_title="Chat with Agent", page_icon="💬")

API_ENDPOINT = "http://host.docker.internal:8002/chat"


# Send message to API
def send_message_to_api(messages: List[Dict[str, str]]) -> str:
    try:
        payload = {"messages": messages}
        response = requests.post(
            API_ENDPOINT,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=30,
        )
        response.raise_for_status()
        return response.json().get("response", "No response received")
    except requests.exceptions.RequestException as e:
        return f"Error communicating with API: {str(e)}"
    except json.JSONDecodeError:
        return "Error: Invalid response from API"


# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages with default Streamlit style (no custom background or icons)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input area at the bottom
st.markdown(
    """
    <style>
    textarea {
        border-radius: 1em !important;
        color: #fff !important;
    }
    </style>
    <script>
    // Focus the chat input automatically on page load and after each rerun
    window.addEventListener('DOMContentLoaded', function() {
        const input = document.querySelector('textarea');
        if(input) input.focus();
    });
    // Also try to focus after each Streamlit update
    new MutationObserver(() => {
        const input = document.querySelector('textarea');
        if(input) input.focus();
    }).observe(document.body, {childList: true, subtree: true});
    </script>
""",
    unsafe_allow_html=True,
)

prompt = st.chat_input("Ask me anything...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.spinner("Getting response..."):
        api_response = send_message_to_api(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": api_response})
    with st.chat_message("assistant"):
        st.markdown(api_response)

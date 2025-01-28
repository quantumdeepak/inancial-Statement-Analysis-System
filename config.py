import os
from dotenv import load_dotenv
import streamlit as st

def load_api_keys():
    """Load API keys from .env file or Streamlit secrets"""
    if os.path.exists(".env"):
        load_dotenv()
    
    # Initialize session state for API keys if not exists
    if 'api_keys_set' not in st.session_state:
        st.session_state.api_keys_set = False

def init_api_keys():
    """Initialize API keys in Streamlit session state"""
    if not st.session_state.api_keys_set:
        # Create columns for API key inputs
        col1, col2 = st.columns(2)
        
        with col1:
            gemini_key = st.text_input("Enter Gemini API Key:", type="password")
        with col2:
            llama_key = st.text_input("Enter LlamaParse API Key:", type="password")
            
        if st.button("Save API Keys"):
            if gemini_key and llama_key:
                st.session_state.gemini_api_key = gemini_key
                st.session_state.llama_api_key = llama_key
                st.session_state.api_keys_set = True
                st.success("API keys saved successfully!")
                st.rerun()
            else:
                st.error("Please enter both API keys")
                
        return False
    
    return True
import streamlit as st
from typing import List

class ChatInterface:
    def __init__(self, query_engine):
        self.query_engine = query_engine
        
        # Initialize chat history if not exists
        if "messages" not in st.session_state:
            st.session_state.messages = []
    
    def display_chat_history(self):
        """Display chat history"""
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    def process_user_input(self, user_input: str):
        """Process user input and generate response"""
        if user_input:
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # Get response from query engine
            response = self.query_engine.query(user_input)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": str(response)})
    
    def clear_chat_history(self):
        """Clear chat history"""
        st.session_state.messages = []
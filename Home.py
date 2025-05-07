import streamlit as st

# Set up page title and description
st.title("Welcome to the Generative AI Startup Idea Generator")
st.write(
    """
    This app helps you generate startup ideas and detailed plans based on your input.
    Select a mode from the sidebar to get started.
    """
)

# Add footer with your name
st.markdown("<br><br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Made by Ammar Ullah Khan</p>", unsafe_allow_html=True)


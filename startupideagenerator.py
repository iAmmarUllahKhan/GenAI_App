import streamlit as st
import requests

# Function to call Gemini 2.0 Flash API using raw HTTP request
API_KEY = "AIzaSyC1-Io5Rol75D4Jcp67nx6ZHdYRHvZp2Ss" # Add your API key to secrets.toml

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

headers = {
    "Content-Type": "application/json"
}

def get_startup_idea(user_input):
    payload = {
        "contents": [{
            "parts": [{
                "text": f"Generate a startup idea and plan for the following problem: {user_input}"
            }]
        }]
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"Error: {response.status_code} - {response.text}"

# Page content and UI elements
st.title("Startup Idea Generator")

st.write(
    """
    Provide a problem or theme, and this tool will generate a startup idea and business plan to solve it.
    """
)

# Input from user
user_input = st.text_input("What problem are you trying to solve?", "")

# Button to trigger idea generation
if st.button("Generate Startup Idea"):
    if user_input:
        with st.spinner("Generating startup idea..."):
            startup_idea = get_startup_idea(user_input)
            st.markdown("### Generated Startup Idea:")
            st.markdown(startup_idea)
    else:
        st.warning("Please enter a problem to solve.")

# Footer with your name
st.markdown("<br><br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Made by Ammar Ullah Khan</p>", unsafe_allow_html=True)


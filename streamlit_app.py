import streamlit as st
import google.generativeai as genai

st.title("🎈 My chatbot")
title = st.text_input("You", "Hello world")
st.write("Your current title is", title)

#Initialize session state for storing chat history if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Initialize with an empty list

#Input field for Gemini API Key
gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here...", type="password")

#Authenticate with the API service and configure the Gemini model
model = None  # Initialize model variable
if gemini_api_key:
    try:
        genai.configure(api_key="AIzaSyAKsMIpDmjb5Z7ydSkwOmyH4Ebj_K-8l3o")  # Use user-provided API key
        model = genai.GenerativeModel("gemini-pro")  
        st.success("API Key validated successfully!")
    except Exception as e:
        st.error(f"An error occurred while setting up the Gemini model: {e}")

#Capture user input using st.chat_input
user_input = st.chat_input("Type your message here...")

#Generate AI response and update chat history
if user_input:
    #Append user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    #Generate AI response using the configured model
    if model:
        try:
            response = model.generate_content(user_input)
            bot_response = response.text

            #Append AI response to chat history
            st.session_state.chat_history.append({"role": "assistant", "content": bot_response})
        except Exception as e:
            st.error(f"An error occurred while generating the response: {e}")

#Display chat messages using st.chat_message
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])
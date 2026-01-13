import streamlit as st
import google.generativeai as genai

st.title("Welcome to the Streamlit App")

user_input= st.text_input("Ask me anything: ")
genai.configure(api_key="AIzaSyAgSyrrUBEAue-ynNeanuZjIcF6Y7IF1Gw")
model=genai.GenerativeModel("models/gemini-3-flash-preview")

if user_input:
    response=model.generate_content(user_input)
    st.write("Response: ",response.text)
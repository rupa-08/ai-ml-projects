import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

st.title("Email classification")

email_input = st.text_area("Please enter your email below: ")

if st.button("Classify"):
    prompt = f"""
    You are an email classification system designed to categorize emails as either Spam or Ham.
    Your job is simple: Spam refers to unwanted, irrelevant, or potentially harmful emails like 
    promotional offers, phishing attempts, or scam messages. Ham, on the other hand, refers to 
    legitimate, non-malicious emails such as personal messages, work-related communication, or 
    general inquiries. When given an email, focus on the content and ignore details like the 
    subject line or sender. If the email includes signs of fraud, urgent actions, or suspicious 
    links, classify it as Spam. If it’s a normal, conversational email, or related to work, classify 
    it as Ham. Always reply with only the words “Spam” or “Ham”, no additional explanation. Make sure 
    your classification is precise and based only on the body of the email.

    Email: {email_input}

    Your response should be in JSON format, like this:
    {{
        "email_type": "spam" or "ham",
        "reason": "Always give brief explanation of why it is classified as spam or ham"
    }}
    """
    
    user_prompt = [{
        "role":"user",
        "content": prompt
    }]

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages = user_prompt,
        max_tokens = 500,
        temperature=1.2
    
    )

    ai_response = response.choices[0].message.content
    st.write("AI Response:")
    st.text(ai_response)

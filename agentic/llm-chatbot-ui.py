
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

#loading api key
load_dotenv()
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
MODEL="llama3-70b-8192"

#streamlit sessions state for chathistory
if "messages" not in st.session_state:
    st.session_state["messages"]=[{
        "role":"system",
        "content":"You are very helpful assistant. Your name is Chatbot. Whatever user asks, you help them in a helpfulway."
        }]

#streamlit UI
st.title("Chat Bot")

for msg in st.session_state["messages"][1:]: 
    sender = "You" if msg["role"] == "user" else "Chatbot"
    st.markdown(f"**{sender}:** {msg['content']}")


col1, col2 = st.columns([6, 1])
with col1:
    user_input = st.text_input("You:", label_visibility="collapsed", key="user_input", placeholder="Type your message...")

with col2:
    send = st.button("Send")

if send and user_input.strip():
    user_input = st.session_state.user_input.strip()

    if user_input:
        st.session_state["messages"].append({
            "role":"user",
            "content":user_input
        })

        client = Groq(api_key=GROQ_API_KEY)

        response = client.chat.completions.create(
            model=MODEL,
            messages=st.session_state["messages"]
        )

        # response
        res = response.choices[0].message.content

        # Append res
        st.session_state["messages"].append({
            "role": "assistant",
            "content": res
        })
    st.rerun()


import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_community.utilities import SerpAPIWrapper
from langchain.tools import Tool
from langchain.agents import initialize_agent

load_dotenv()
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
SERP_API_KEY=os.getenv("SERPAPI_API_KEY")
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


col1, col2, col3 = st.columns([8, 1, 1])

with col1:
    user_input = st.text_input("You:", label_visibility="collapsed", key="user_input", placeholder="Type your message...")

with col2:
    send = st.button("Send")

with col3:
    web = st.button("Web")

if send and user_input.strip():
    user_input = user_input.strip()

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

# For web search
if web and user_input.strip():
    user_input = user_input.strip()

    if user_input:
        st.session_state["messages"].append({
            "role":"user",
            "content":user_input
        })

        groq_llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model=MODEL,
        temperature=1.0,
        max_tokens=500
    )
    search = SerpAPIWrapper(serpapi_api_key=SERP_API_KEY)

    search_tool = Tool(
        name="Web Search",
        func=search.run,
        description="Searches web for latest information.",
        handle_parsing_errors=True
    )

    agent = initialize_agent(
        tools=[search_tool],
        llm=groq_llm,
        #verbose=True
    )
    response = agent.run(user_input)

    st.session_state["messages"].append({
        "role":"assistant",
        "content": response
    })
    st.rerun()




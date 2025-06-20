from dotenv import load_dotenv
import os
from groq import Groq
import streamlit as st
from pinecone import Pinecone
from create_vectors import embed_text

load_dotenv()
PINECONE_API_KEY = os.getenv("PINE_CONE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

pinecone_client = Pinecone(api_key=PINECONE_API_KEY)   # Initialize Pinecone client
vector_index = pinecone_client.Index("first-kb")       # Connect to existing Pinecone index

groq_client = Groq(api_key=GROQ_API_KEY)               # Initialize Groq client for LLM

st.title("Frist RAG App")
st.write("This is RAG app that uses Pineconde and Groq for answering questions based on the documents in the ")

query = st.text_input("Enter questions about people: ")

if st.button("Submit"):
    vector = embed_text(query).get("embedding", [])    # Convert user query into embedding using Gemini
    response = vector_index.query(                     # Query Pinecone index for most similar documents
        vector=vector,
        top_k=1,                                       # Also get the original text stored with the document
        include_metadata=True
    )

    #get first document which matches most 
    # similar_document = response["matches"][0]["metadata"]["text"]

    # to get all similar document
    similar_document = ""                              # store the similar document text here
    for match in response["matches"]:                  # Loop through matched documents from Pinecone
        text = match["metadata"]["text"]               # Extract original text from metadata
        similar_document += text + "\n"                # Combine all matched texts

    print("Similar document: ", similar_document)

    prompt = [
        {
            "role":"user",
            "content":f"""You are provided with some document sample which to be most similar document which can be  expected to be most similar .
            If you find something relevent in the similar document, use a context to answer the user query.
            If the question is not about the document, as a helpful assistant, you should provide answer based on your knowledge and please don't share anything realted to document if user query is not releted to document.
            Similar Document: {similar_document}∆∆∆
            User query: {query}
            """
        }]

    print("Prompt: ", prompt)

    # Send the prompt to Groq’s AI model (LLaMA3)
    llm_response = groq_client.chat.completions.create(
        model="llama3-70b-8192",
        messages=prompt,
        max_tokens=500,             # limit length of AI response
        temperature=0.7             #creativity/randomness
    )

    llm_answer = llm_response.choices[0].message.content   # Extract the final generated answer
    st.write("Answer: ", llm_answer)
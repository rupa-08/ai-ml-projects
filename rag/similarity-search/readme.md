# Question Answering with Pinecone & Groq

This project is a **Retrieval-Augmented Generation (RAG)** app that allows users to ask questions based on the contents of uploaded PDF documents. It uses **Pinecone** for vector storage and search, **Google Gemini** for embedding text, and **Groq (LLaMA 3)** for answering the questions in natural language. The app is built using **Streamlit** for a simple web interface.

---

## 📋 What This Project Does

1. **Document Ingestion**:
   - Reads PDF documents from a folder (`/documents`).
   - Extracts text from each file using PyMuPDF (`fitz`).
   - Converts that text into vector embeddings using **Google Gemini embeddings**.

2. **Indexing in Pinecone**:
   - Stores the text vectors in a Pinecone index (`first-kb`) with metadata.

3. **Interactive Q&A App**:
   - Users enter a question into the Streamlit UI.
   - The app embeds the query and searches the most relevant documents in Pinecone.
   - It then feeds the relevant text and question to **Groq’s LLaMA 3 model** to generate an intelligent, context-aware answer.

---

## 💡 Prompt Engineering – In Simple Words

Prompt engineering is like **giving clear instructions to an AI assistant**. Here’s how it’s done in this project:

- You give the AI model two things:
  - **Relevant document text** (found using Pinecone).
  - **Your actual question**.
- The model uses the document as a reference to give a **smart, relevant, and accurate** answer.

Example of the prompt:
```
You are provided with some document sample...
If you find something relevant in the similar document, use it to answer the user query.
Similar Document: [text]
User query: [question]
```

This helps the AI "think" with your documents instead of answering from general knowledge.

---

## Technologies Used

| Tool/Library            | Purpose                                                  |
|-------------------------|----------------------------------------------------------|
| `pinecone`              | Stores and searches document embeddings (vectors).       |
| `google-generativeai`   | Converts text into vector embeddings using Gemini.       |
| `groq`                  | Sends the prompt to Groq’s fast LLaMA 3 model.           |
| `fitz` (PyMuPDF)        | Used for reading PDF documents and extracting text from them.                                 |
| `streamlit`             | Creates a simple, interactive frontend for users.        |
| `dotenv`                | Loads secret API keys from a `.env` file securely.       |


---

## 📦 Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/your-username/ask-my-docs.git
cd ask-my-docs
```

2. **Create Python Environment**
New virtual environment using `conda`:
```bash
conda create --name agents python=3.12
conda activate agents
```

3. **Install dependencies**
```bash
pip install pinecone-client google-generativeai PyMuPDF python-dotenv groq streamlit
```

4. **Create `.env` file**
```env
PINE_CONE_API_KEY=your_pinecone_api_key
GEMINI_API_KEY=your_google_gemini_api_key
GROQ_API_KEY=your_groq_api_key
```
---

## Run the App

### 1. Index the documents (run once)
```bash
python create_vectors.py
```

### 2. Start the Streamlit app
```bash
streamlit run rag_app.py
```

---

## Example Use

> 👤 You: *"Who is Rupa?"*  
> 🤖 AI: *"Rupa is a person mentioned in the document. She wrote about..."*

It smartly pulls answers from your own documents!

---

## Future Improvements

- Add support for more file types (e.g., Word, TXT)
- Allow multiple top-k matches
- Support follow-up Q&A (chat mode)

---

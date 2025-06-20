from pinecone import Pinecone
import fitz
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
PINECONE_API_KEY=os.getenv("PINE_CONE_API_KEY")
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

model = "models/text-embedding-004"                    # embedding model

genai.configure(api_key=GEMINI_API_KEY)                # Configure the Gemini API with your key

pinecone_client = Pinecone(api_key=PINECONE_API_KEY)   # initialize pinecone api key
vector_index = pinecone_client.Index("first-kb")       # connect to pinecode index

# Function to extract all text from a PDF (from all pages)
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:                               # Loop through each page
            text += page.get_text() + "\n"             # get all text from pdf and store in text variable
    return text

# text embedding func using Gemini
def embed_text(text):
    res = genai.embed_content(
        model=model,
        content=text,
        task_type="retrieval_document",                # type based on task you want to perform
    )
    return res

def upsert_vectors_to_pinecone(document_text):
    
    upsert_data = []                                   # data to be sent to pinecone

    for index, (file, text) in enumerate(document_text.items()):
        vector = embed_text(text).get("embedding", []) # to get embedded vector of the text using gemini
        
        meta_data = {
            "text": text,                              # metadata to store with vector, here only original text is used
        }
        upsert_data.append((f"doc-{index}", vector, meta_data))  # Append a tuple: (ID, vector, metadata) to the upsert list

    vector_index.upsert(upsert_data)                   # Send the list of vectors and metadata to Pinecone
    print("Vectors upserted successfully.")

# This block runs only if the script is executed directly (not imported as a module)
if __name__ == "__main__":
    document_text = {}                                 # Dictionary to hold filenames and their extracted text

    for file in os.listdir("documents"):
        text = extract_text_from_pdf("documents/" + file)  # Extract text from each PDF file
        document_text[file] = text                     # Store the text in the dictionary with the filename as the key

    upsert_vectors_to_pinecone(document_text)          # Send the text data to Pinecone as vectors (embeddings)
    print("All documents processed and vectors upserted.")


#document_text brefore putting it into upsert_vectors_to_pinecone
# {
#     "bikesh.pdf":"his texts",
#     "rupa.pdf":"her texts",
#     "salini.pdf":"her texts"
# }
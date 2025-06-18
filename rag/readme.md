
### Step-by-step Explanation
1. **PDF → Text**  
   First, we extract text from PDF files.  
   If the PDF is a scanned file (like image or photo), it needs **OCR (Optical Character Recognition)** to convert the image into readable text.

2. **Text → Embedding**  
   The text is converted into **embeddings** — these are number representations of text that capture the meaning.

3. **Embedding → Vectors**  
   Embeddings are stored as **vectors** (lists of numbers) so that we can compare them mathematically.

4. **Vectors → Pinecone**  
   These vectors are saved in **Pinecone**, a fast vector database.  
   When the user asks a question, we also embed the question and find the most similar document from Pinecone.

---

### Notes

- **Searchable document** → A PDF where text can be selected or copied. No need for OCR.
- **Scanned document** → A PDF made from images (like scanned pages). Needs OCR to read text.
- **Similarity search** → A method to find which document is closest in meaning to the user's query using vectors and embeddings.


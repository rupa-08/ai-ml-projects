# Sentiment Analysis Web App Using Streamlit
 
This is a simple project created for learning purposes. In this project, I built a **Sentiment Analysis** web application using **Python**, **Scikit-learn**, and **Streamlit**.

I trained a machine learning model in a Jupyter Notebook, saved it using `pickle`, and then used it in the web app to predict the sentiment of any text you provide.

---

## 📝 About the Project

This is a basic **NLP (Natural Language Processing)** project, where the goal is to classify the sentiment of a sentence — whether it’s **positive**, **negative**, or **neutral** (depending on the dataset you use). The model understands human language at a basic level and predicts the sentiment accordingly.

- The model is trained in a **Jupyter Notebook** (`Sentiment-analysis.ipynb`).
- The trained model and vectorizer are serialized (saved) using `pickle`.
- A **Streamlit** web app is used to serve the model and allow users to input text.

---

## 🛠️ Technologies Used

- **Python 3**
- **Jupyter Notebook** – for training the model
- **scikit-learn** – for machine learning and text vectorization
- **NLTK** – for natural language preprocessing (tokenization, stopwords removal, etc.)
- **Streamlit** – for creating the web interface
- **Pickle** – for saving and loading the trained model and vectorizer

---

## 🤖 How It Works

### Training the Model:
- The model is trained using a **text dataset**.
- The text is first **preprocessed** (tokenization, stopwords removal, etc.), and then **vectorized** using **TF-IDF** or **CountVectorizer**.
- The sentiment is predicted using a classifier such as **Logistic Regression**.

### Streamlit Web App:
- The app allows users to **input text**.
- The text is **preprocessed** and **vectorized** using the same steps as in training.
- The **preprocessed text** is passed to the model for sentiment prediction.
- The result (**Positive**/**Negative**) is displayed to the user in **real-time**.

---

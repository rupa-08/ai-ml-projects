# BBC News Classification

This project is a text classification system that categorizes BBC news articles into predefined categories using machine learning techniques.

It uses:

- **Scikit-learn (Naive Bayes classifier)** for model training
- **TF-IDF Vectorizer** for feature extraction
- **Streamlit** for the user interface
- **NLTK** for text preprocessing (lemmatization, stopword removal, tokenization)

---

## 📌 Features

- Classifies news into categories based on their content (e.g., business, sport, tech, etc.)
- Interactive UI built with Streamlit for real-time predictions
- Uses pre-trained model and vectorizer saved as `.pkl` files

---

## 🧠 Model Training

The model is trained using the `bbc_data.csv` dataset with the following pipeline:

1. Preprocess text (lowercase, remove punctuation, lemmatize, remove stopwords)
2. Transform text using TF-IDF vectorizer
3. Train a `MultinomialNB` classifier
4. Evaluate using classification report and confusion matrix
5. Save the model and vectorizer using `pickle`

---
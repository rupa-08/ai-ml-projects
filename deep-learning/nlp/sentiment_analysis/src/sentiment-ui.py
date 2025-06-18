import streamlit as st
import pickle
import re

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

st.title("Sentiment Analysis")
st.write("This app uses a Naive Bayes Classifier to predict sentiment from text.")

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english')) 


with open('sentiment_model.pkl','rb') as file:
    senti_model = pickle.load(file)

with open('sentiment_vectorizer.pkl','rb') as file:
    vectorizer = pickle.load(file)

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]','',text)
    tokens = word_tokenize(text)
    cleaned = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(cleaned)
    
user_input = st.text_input("Enter your text here:")

predict_btn = st.button("Predict")

if predict_btn:
    preprocessed_text = preprocess(user_input)
    vectorized_text = vectorizer.transform([preprocessed_text])
    prediction = senti_model.predict(vectorized_text)
    st.write("Prediction:",prediction[0] )
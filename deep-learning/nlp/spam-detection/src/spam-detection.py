import streamlit as st
import pickle
import re

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

st.title("Spam Detection")
st.write("For spam detection")

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

with open('model.pkl','rb') as file:
    model = pickle.load(file)

with open('vectorizer.pkl','rb') as file:
    vectorizer = pickle.load(file)

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]','',text)
    tokens = word_tokenize(text)
    cleaned = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(cleaned)

user_input = st.text_input("Email content:")
predict_btn = st.button("Predict")

if predict_btn:
    preprocessed_text = preprocess(user_input)
    vectorized_text = vectorizer.transform([preprocessed_text])
    prediction = model.predict(vectorized_text)
    st.write("Prediction: ", prediction[0])
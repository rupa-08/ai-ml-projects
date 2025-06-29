import streamlit as st
import numpy as np 
from tensorflow.keras.models import load_model
from PIL import Image
import os
import pickle

st.title("Vehicle Classification")

model = load_model('model.h5')
with open("class_names.pkl", "rb") as f:
    class_names = pickle.load(f)

file = st.file_uploader("Upload image: ", type=['jpg','jpeg','png'])

if file is not None:
    image = Image.open(file) 
    st.image(image, caption='Uploaded Image', use_column_width=True)

    #prerpocess image
    image = image.resize((224, 224))  # Resize image if necessary
    image_array = np.array(image) / 255.0  # Normalize the image
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

    # Predict using the loaded model
    prediction = model.predict(image_array)
    predicted_class = np.argmax(prediction, axis=1)  # Get class with highest probability

    # Display the prediction
    predicted_label = class_names[predicted_class[0]]
    st.write(f"Predicted Class: {predicted_label}{predicted_class[0]}")

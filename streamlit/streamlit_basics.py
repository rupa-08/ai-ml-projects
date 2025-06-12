import streamlit as st
import pandas as pd
from PIL import Image

# TITLE & SUBHEADER
st.title("Hello Data Science Class!")
st.subheader("This is a subheader")
st.text("Text area to describe thoughts.")
st.write("This is written using st.write.")

# MARKDOWN
st.markdown("### Welcome")
st.markdown("> Blockquote style text")
st.markdown("### This is a markdown")

# STATUS MESSAGES
st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")

# SELECTBOX
selected = st.selectbox("Please select: ", ['Option 1', 'Option 2', 'Option 3'])
st.write(f"Selected option: {selected}")

# BUTTON
if st.button("Submit"):
    st.success("Option has been selected.")

# CHECKBOX
checkbox_option = st.checkbox("Add masala")
if checkbox_option:
    st.write("Masala has been selected.")

# RADIO
radio_options = st.radio("Pick an option: ", ['Option A', 'Option B', 'Option C'])
st.write(f"Selected: {radio_options}")

# SLIDER
slider_val = st.slider("Slider level:", 0, 5, 3)
st.write(f"Slider selected: {slider_val}")

# NUMBER INPUT
num_val = st.number_input("Enter a number:", min_value=1, max_value=10, step=1)
st.write("Selected number:", num_val)

# TEXT INPUT
name = st.text_input("Enter your name:")
if name:
    st.write(f"Welcome, {name.title()}")

# DATE INPUT
dob = st.date_input("Select your DOB:")
st.write(f"Your DOB is: {dob}")

# COLUMNS
col1, col2 = st.columns(2)
with col1:
    st.subheader("Col 1")
    st.image("https://imgs.search.brave.com/Xr7tVBYQPFX-RIP_rpREgCRVuQZ2XxMM7p2S3z1PaRg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90aHVt/YnMuZHJlYW1zdGlt/ZS5jb20vYi9ibHVy/cmVkLXNwcmluZy1h/dXR1bW4tbmF0dXJl/LWJhY2tncm91bmQt/Z3JlZW4tc3Vubnkt/ZmllbGQtdHJlZS1i/bHVlLXNreS1vdXRk/b29yLTUzOTAyNTI3/LmpwZw", width=200)
    vote1 = st.button("Vote 1")

with col2:
    st.subheader("Col 2")
    st.image("https://imgs.search.brave.com/Xr7tVBYQPFX-RIP_rpREgCRVuQZ2XxMM7p2S3z1PaRg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90aHVt/YnMuZHJlYW1zdGlt/ZS5jb20vYi9ibHVy/cmVkLXNwcmluZy1h/dXR1bW4tbmF0dXJl/LWJhY2tncm91bmQt/Z3JlZW4tc3Vubnkt/ZmllbGQtdHJlZS1i/bHVlLXNreS1vdXRk/b29yLTUzOTAyNTI3/LmpwZw", width=200)
    vote2 = st.button("Vote 2")

if vote1:
    st.write("You voted for option 1.")
elif vote2:
    st.write("You voted for option 2.")

# SIDEBAR
your_name = st.sidebar.text_input("Enter your name:")
your_option = st.sidebar.selectbox("Select an option:", ['Option 1', 'Option 2', 'Option 3'])
if your_name:
    st.sidebar.write(f"Hello {your_name}, you selected {your_option}.")

# EXPANDER
with st.expander("Follow instructions"):
    st.write("""
    Step 1: First step  
    Step 2: Second step  
    Step 3: Third step
    """)

# FILE UPLOAD
st.subheader("Upload a CSV file")
file = st.file_uploader("Choose a CSV file:", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.success("File uploaded successfully!")
    st.dataframe(df)
    st.write(df.describe())

# IMAGE UPLOAD (LOCAL)
try:
    img = Image.open("sample_image_1.webp")
    st.image(img, width=200)
except:
    st.warning("Local image 'sample_image_1.webp' not found.")

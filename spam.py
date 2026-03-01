import streamlit as st
import pickle
import re
import string

# Load the trained model and vectorizer
with open("spam_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Function to clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
    text = text.strip()  # Remove extra spaces
    return text

# Streamlit UI
st.title("Spam Mail Detection (Subject Line)")
st.write("Enter the subject of an email to check if it's spam or not.")

# User input
subject = st.text_input("Enter email subject:")

if st.button("Check"):
    if subject:
        cleaned_subject = clean_text(subject)
        transformed_subject = vectorizer.transform([cleaned_subject])
        prediction = model.predict(transformed_subject)

        if prediction[0] == 1:
            st.error("🚨 This is SPAM!")
        else:
            st.success("✅ This is NOT spam.")
    else:
        st.warning("Please enter an email subject.")


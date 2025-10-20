# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 20:44:30 2025

@author: rains
"""

import streamlit as st
import pickle
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
import re
import nltk

# Download NLTK data
nltk.download('stopwords')

# Initialize stemmer
ps = PorterStemmer()

# -----------------------
# Text Preprocessing
# -----------------------
def transform_text(text):
    text = text.lower()  # lowercase
    text = re.findall(r'\b\w+\b', text)  # tokenize words (alphanumeric only)
    
    y = []
    for i in text:
        if i.isalnum():  # keep only alphanumeric tokens
            y.append(i)
    
    text = [i for i in y if i not in stopwords.words('english') and i not in string.punctuation]
    
    # Apply stemming
    text = [ps.stem(i) for i in text]
    
    return " ".join(text)

# -----------------------
# Load Model and Vectorizer
# -----------------------

tfidf = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("model.pkl", 'rb'))

# -----------------------
# Streamlit App
# -----------------------
st.title("📩 Email/SMS Spam Classifier")

# Text input
input_text = st.text_area("Enter the message:")

# Predict button
if st.button("Predict"):
    if input_text.strip() == "":
        st.warning("⚠️ Please enter a message.")
    else:
        transformed = transform_text(input_text)
        vectorized = tfidf.transform([transformed])
        prediction = model.predict(vectorized)[0]
        
        if prediction == 1:
            st.error("Spam")
        else:
            st.success("Not Spam")




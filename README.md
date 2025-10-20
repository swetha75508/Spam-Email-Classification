# 📩 Email/SMS Spam Classifier

A simple and interactive **Streamlit web app** that classifies text messages (Emails or SMS) as **Spam** or **Not Spam** using Natural Language Processing (NLP) and Machine Learning techniques.

---

## 🚀 Project Overview

This project uses a **Logistic Regression model** trained on text message data to detect spam.  
The web interface is built with **Streamlit**, making it easy for users to input messages and get instant predictions.

---

## 🧠 Tech Stack

- **Python**
- **Streamlit** – for building the interactive UI  
- **Scikit-learn** – for machine learning  
- **NLTK** – for text preprocessing  
- **Pickle** – for saving and loading the model and vectorizer  

---

## ⚙️ Features

✅ Clean and simple user interface  
✅ Real-time spam prediction  
✅ Text preprocessing with stemming and stopword removal  
✅ Model and vectorizer loading via pickle  
✅ Works with both emails and SMS  

---

## 🧹 Text Preprocessing Steps

1. Convert text to lowercase  
2. Tokenize text using regular expressions  
3. Remove stopwords, punctuation, and special characters  
4. Apply stemming using **PorterStemmer**  
5. Transform using **TF-IDF Vectorizer**

---

## 🧾 Project Structure

📂 spam-classifier/
│
├── app.py # Streamlit application file
├── model.pkl # Trained machine learning model
├── vectorizer.pkl # TF-IDF vectorizer
├── requirements.txt # Dependencies
└── README.md # Project documentation

# 📩 Email/SMS Spam Classifier

A simple and interactive **Streamlit web app** that classifies text messages (Emails or SMS) as **Spam** or **Not Spam** using Natural Language Processing (NLP) and Machine Learning techniques.

---

## 🚀 Project Overview

This project uses a **Naive Bayes Model** trained on  SMS/Email text data to detect spam messages.  
The web interface is built with **Streamlit**, allowing users to easily input messages and get real-time predictions.

---

## 🧠 Tech Stack

- **Python**
- **Streamlit** – for the web interface  
- **Scikit-learn** – for machine learning  
- **NLTK** – for text preprocessing  
- **Pickle** – for saving and loading the model and vectorizer  

---

## ⚙️ Features

✅ Clean and simple user interface  
✅ Real-time spam classification
✅ Text preprocessing  (tokenization, stopword removal, stemming)  
✅ Uses **TF-IDF** features and **Naive Bayes** model  
✅ Works for both **emails** and **SMS messages**  

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




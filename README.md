# 📧 Spam Mail Detection using Machine Learning

## 📌 Overview

This project is a **Spam Mail Detection System** built using **Python** and **Machine Learning**. It classifies emails as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) techniques and an SVM model.

---

## 🚀 Features

* Detects spam and non-spam emails
* Uses TF-IDF vectorization
* Trained using Support Vector Machine (SVM)
* High accuracy model
* Simple and easy to use
* Model saved using pickle for reuse

---

## 🛠️ Technologies Used

* Python
* Scikit-learn
* Pandas
* NumPy
* TF-IDF Vectorizer
* Support Vector Machine (SVM)
* Jupyter Notebook

---

## 📂 Project Structure

```
SPAM_MAIL_DETECTION/
│
├── Emails.csv                # Dataset
├── spam-mail.ipynb          # Training notebook
├── spam.py                  # Python script
├── spam_model.pkl           # Trained model
├── vectorizer.pkl           # TF-IDF vectorizer
├── tfidf_vectorizer.joblib  # Saved vectorizer
├── SVM_linear_best_*.pkl    # Best trained model
└── README.md                # Project documentation
```

---

## ⚙️ Installation

### Step 1: Clone repository

```
git clone https://github.com/YOUR_USERNAME/spam-mail-detection.git
cd spam-mail-detection
```

### Step 2: Install dependencies

```
pip install pandas numpy scikit-learn
```

---

## ▶️ Usage

Run the Python file:

```
python spam.py
```

Example:

```
Input: "Congratulations! You won a free prize"
Output: Spam
```

---

## 🧠 Machine Learning Workflow

1. Load dataset
2. Data preprocessing
3. Text vectorization using TF-IDF
4. Train SVM model
5. Evaluate accuracy
6. Save model and vectorizer

---

## 📊 Model Accuracy

Achieved high accuracy using Linear SVM classifier.

---

## 💾 Saved Files

* spam_model.pkl → trained model
* vectorizer.pkl → TF-IDF vectorizer

---

## 👨‍💻 Author

Ayushman

---

## ⭐ Future Improvements

* Add GUI using Tkinter or Web App
* Deploy using Flask or Streamlit
* Use deep learning models

---

## 📜 License

This project is open source and free to use.

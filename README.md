# 📧 Spam Email Classification App

A Machine Learning web application built with **Streamlit** to classify emails as **Spam** or **Ham (Not Spam)** in real-time.

This project demonstrates the complete Machine Learning workflow from model training to web deployment.

---

## 🚀 Live Demo

🔗 https://spamemaildetectionapps.streamlit.app/

---

## 🧠 Project Overview

Spam detection is a classic Natural Language Processing (NLP) problem.  
This application allows users to input email text and receive an instant prediction indicating whether the email is Spam or not.

The model provides:
- Predicted label (Spam / Ham)
- Confidence score (probability)

---

## ✨ Features

- 📥 Text-based email input
- ⚡ Real-time classification
- 📊 Prediction confidence display
- 🎨 Modern custom UI (Silver Grey Theme)
- ☁️ Deployable on Streamlit Cloud

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- Joblib
- Pandas
- NumPy

---

## 📂 Project Structure

```
SpamEmailDetection/
│
├── app.py
├── model.pkl
├── requirements.txt
├── spam.csv
└── README.md
```

---

## ⚙️ Installation (Run Locally)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/nikitabrillian/spam-email-detection.git
cd spam-email-detection
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the App

```bash
streamlit run app.py
```

Open in browser:
```
http://localhost:8501
```

---

## ☁️ Deployment (Streamlit Cloud)

1. Push project to GitHub
2. Go to https://share.streamlit.io
3. Click **New App**
4. Select repository
5. Set main file path to:
```
app.py
```
6. Click **Deploy**

---

## 📊 Model Details

- Model Type: Binary Classification
- Classes:
  - 1 → Spam
  - 0 → Ham (Not Spam)
- Output: Label + Probability Score
- Model stored using Joblib (`model.pkl`)

---

## 🔎 How It Works

1. User enters email text
2. Text is processed by the trained model
3. Model predicts Spam or Ham
4. Application displays the result and confidence score

---

## 📌 Notes

- Ensure `model.pkl` is in the root directory
- Do not upload the `venv/` folder
- Add `venv/` to `.gitignore`
- Model size must be under 100MB for Streamlit Cloud

---

## 👩‍💻 Author

Nikita Amelia Valencia  
Machine Learning & Data Science Enthusiast

---

## 📜 License

This project is for educational and portfolio purposes.

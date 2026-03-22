# AI-Refund-fraud-detection-
An AI-powered fraud detection system for e-commerce platforms that identifies suspicious refund requests using machine learning. By analyzing transactional and behavioral patterns, the model helps reduce financial losses, improve decision-making, and enhance trust with genuine customers.

# 🛒 AI-Powered Refund Fraud Detection System

## 📌 Overview

This project aims to detect fraudulent refund requests in e-commerce platforms using machine learning. Fraudulent refunds cause significant financial losses, and this system helps identify suspicious transactions using behavioral and transactional data.

---

## 🚀 Features

* Detects fraudulent transactions using ML models
* Supports Random Forest and XGBoost
* Handles imbalanced datasets
* Provides performance evaluation (Accuracy, Precision, Recall, F1, ROC-AUC)
* Includes advanced visualizations (ROC Curve, Precision-Recall Curve, Feature Importance)
* Threshold tuning for improved fraud detection

---

## 📊 Dataset

* Source: Kaggle / Simulated E-commerce dataset
* Features include:

  * Transaction Amount
  * Payment Method
  * Device Used
  * Customer Location
  * Account Age
  * Transaction Time

---

## 🤖 Models Used

* Random Forest
* XGBoost

---

## 📈 Results

| Metric    | Random Forest | XGBoost |
| --------- | ------------- | ------- |
| Accuracy  | 0.95          | 0.80    |
| Precision | 0.80          | 0.16    |
| Recall    | 0.14          | 0.66    |
| F1 Score  | 0.24          | 0.25    |
| ROC-AUC   | 0.79          | 0.80    |

✔ XGBoost performs better in detecting fraud due to higher recall.

---

## 🧠 Key Insights

* Fraud transactions are rare (~5%)
* XGBoost captures more fraud cases
* Threshold tuning improves detection performance
* Device, transaction amount, and account age are key indicators

---

## 🔮 Future Enhancements

* Real-time fraud detection
* Deep learning models
* Streamlit dashboard
* User behavior analytics (clickstream)

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Matplotlib, Seaborn

---

## 📂 How to Run

```bash
git clone https://github.com/your-username/AI-Refund-Fraud-Detection.git
cd AI-Refund-Fraud-Detection
pip install -r requirements.txt
python src/main.py
```

---


## 📌 Author

Aayat Nizam

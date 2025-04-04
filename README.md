# 💼 Bank Marketing Campaign Prediction (Machine Learning Model)

## 📌 Project Overview

This project focuses on predicting whether a client will subscribe to a term deposit product offered by a Portuguese bank. The dataset is based on a direct marketing campaign and includes client information, call outcomes, and more.

We built multiple machine learning models, applied **SMOTE** for class imbalance, and performed **hyperparameter tuning** on the best model – Random Forest – to achieve over **93% accuracy**.

---

## 📊 Dataset

- Source: UCI Machine Learning Repository - Bank Marketing Dataset  
- Records: ~41,000 entries after preprocessing
- Target Variable: `y` (Yes = subscribed, No = not subscribed)

---

## 🔧 Tools and Technologies Used

- Python  
- Jupyter Notebook  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib, Seaborn  
- Imbalanced-learn (SMOTE)  

---

## 🧹 Data Preprocessing

- Handled missing values  
- Converted categorical variables using Label Encoding and One-Hot Encoding  
- Feature scaling applied (where required)  
- **SMOTE** used to balance the target class

---

## 🤖 Models Implemented

- Logistic Regression  
- Decision Tree  
- Random Forest  

---

## 🧠 Best Performing Model: Random Forest (With Hyperparameter Tuning)

### 🎯 Performance Metrics (on SMOTE-balanced data)

| Metric               | Value         |
|----------------------|---------------|
| **Accuracy**         | **93.4%**     |
| **Precision**        | 91.2%         |
| **Recall**           | 94.7%         |
| **F1 Score**         | 92.9%         |
| **ROC-AUC Score**    | 0.96          |

- Hyperparameters Tuned:
  - `n_estimators`
  - `max_depth`
  - `min_samples_split`
  - `criterion`

---

## 📈 Confusion Matrix Summary

- **True Positives and Negatives** are high
- **False Negatives** are minimal, which is crucial for targeting real potential customers

---

## 🧠 Key Learnings

- How to handle imbalanced datasets using SMOTE  
- Hyperparameter tuning using GridSearchCV  
- Evaluating models using precision, recall, F1-score, ROC-AUC  
- Importance of data cleaning and feature engineering

---

## 🚀 Future Work

- Deploying model using Streamlit or Flask  
- Integrate with business dashboards (Power BI / Tableau)  
- Automate the pipeline with real-time predictions


---

## 📌 Author

**Anirudha Johare**  
Data Science & Analytics Enthusiast  
📫 [LinkedIn Profile](https://www.linkedin.com/in/anirudhajohare19/)

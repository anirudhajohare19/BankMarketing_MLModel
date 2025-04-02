# 🏦 Bank Tele Marketing Machine Learning Model

## 📊 Predicting Customer Subscription Using ML

### 🔹 Overview

This project focuses on **predicting whether a customer will subscribe to a bank term deposit** based on historical marketing data. We use **Logistic Regression and Random Forest Classifier** to classify customer responses and evaluate model performance using various metrics.

---

## 📂 Dataset Information

- **Dataset:** Bank Marketing Dataset (UCI Repository)
- **Size:** 41,188 rows, 21 features
- **Target Variable:** `y` (Subscribed: Yes/No)

### 🔑 Key Features Used:

✅ Age, Job Type, Marital Status, Education Level\
✅ Default History, Balance, Housing Loan, Personal Loan\
✅ Contact Type, Day of Contact, Month, Campaign Information\
✅ Previous Outcomes & Communication Details

---

## 🚀 Project Workflow

1️⃣ **Data Cleaning & Preprocessing**

- Handled missing values and outliers
- Encoded categorical variables
- Scaled numerical features

2️⃣ **Exploratory Data Analysis (EDA)**

- Visualized customer demographics & marketing campaign success
- Analyzed correlations & key influencing factors

3️⃣ **Feature Engineering**

- One-hot encoding for categorical variables
- Feature scaling using MinMax Scaler

4️⃣ **Model Training & Evaluation**

- **Logistic Regression & Random Forest Classifier**
- **Hyperparameter Tuning for Random Forest**
- Performance evaluation using **Confusion Matrix, AUC-ROC Curve, Precision-Recall**

---

## 📈 Model Performance

| Model               | Accuracy | Precision | Recall | AUC-ROC |
| ------------------- | -------- | --------- | ------ | ------- |
| Logistic Regression | 81.2%    | 87.5%     | 76.8%  | 0.88    |
| Random Forest       | 89.2%    | 89.3%     | 80.2%  | 0.91    |

**🔹 Insights:**\
✅ Random Forest performed better in terms of recall and AUC-ROC.\
✅ The marketing campaign success rate is influenced by previous interactions and customer demographics.

---


## 💡 Key Learnings

✅ Importance of feature engineering in improving model accuracy.\
✅ How to evaluate models using AUC-ROC & precision-recall metrics.\
✅ How marketing campaign strategies impact customer decisions.

---

## 👨‍💻 Project By 

**Anirudha Johare**

- 📧 [Email] : anirudhajohare@gmail.com
- 🔗 [LinkedIn]: https://www.linkedin.com/in/anirudhajohare/



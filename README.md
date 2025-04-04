# 🏦 Bank Tele Marketing Machine Learning Model

This project aims to predict whether a client will subscribe to a term deposit based on the Bank Marketing dataset using supervised machine learning models. It includes end-to-end steps from data cleaning, EDA, preprocessing, model training, evaluation, and tuning.

## 📌 Problem Statement

A Portuguese banking institution wants to identify clients who are likely to subscribe to a term deposit. The goal is to build a predictive model that can assist in improving their marketing campaign effectiveness.


## 📊 Predicting Customer Subscription Using ML


---

## 📂 Dataset Information

- **Source**: UCI Machine Learning Repository - [Bank Marketing Dataset](https://archive.ics.uci.edu/ml/datasets/bank+marketing)
- **Total Rows and Columns**: ~41,000 and 21 
- **Target Variable**: `y` – Whether the client subscribed (`yes` or `no`)


### 🔑 Key Features Used:

✅ Age, Job Type, Marital Status, Education Level\
✅ Default History, Balance, Housing Loan, Personal Loan\
✅ Contact Type, Day of Contact, Month, Campaign Information\
✅ Previous Outcomes & Communication Details

---

## 🔍 Key Steps Performed

### 1. 📊 Exploratory Data Analysis (EDA)
- Statistical summaries and missing values check
- Visual distribution of categorical variables
- Correlation heatmap of numerical features

### 2. 🧼 Preprocessing
- Label encoding of categorical columns
- Feature scaling with `StandardScaler`

### 3. 🤖 Model Building
Trained and evaluated the following models:
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier

### 4. ✅ Evaluation Metrics
- Confusion Matrix
- Classification Report (Precision, Recall, F1-score)
- ROC-AUC Score & ROC Curve

### 5. 🔧 Hyperparameter Tuning
- Used `GridSearchCV` on Random Forest for optimal parameter selection

---

## 📈 Results

| Model              | Accuracy | Precision | Recall | ROC-AUC |
|-------------------|----------|-----------|--------|---------|
| Logistic Regression | ~88%    | Good      | Good   | Good    |
| Random Forest       | ~90%+   | Better    | Better | Better  |
| XGBoost             | ~90%+   | Best      | Best   | Best    |


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



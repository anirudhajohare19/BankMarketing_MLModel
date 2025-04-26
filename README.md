#  Bank Tele Marketing Machine Learning Model

This project focuses on predicting whether a client will subscribe to a term deposit product offered by a Portuguese bank. The dataset is based on a direct marketing campaign and includes client information, call outcomes, and more.

We built multiple machine learning models, applied **SMOTE** for class imbalance, and performed **hyperparameter tuning** on the best model – Random Forest – to achieve over **93% accuracy**.

---

##  Dataset

- Source: UCI Machine Learning Repository - Bank Marketing Dataset  
- Records: ~41,000 entries after preprocessing
- Target Variable: `y` (Yes = subscribed, No = not subscribed)

---

##  Tools and Technologies Used

- Python  
- Jupyter Notebook  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib, Seaborn  
- Imbalanced-learn (SMOTE)  

---

##  Key Steps Performed

### 1.  Exploratory Data Analysis (EDA)
- Statistical summaries and missing values check
- Visual distribution of categorical variables
- Correlation heatmap of numerical features

### 2.  Preprocessing
- Label encoding of categorical columns
- Feature scaling with `MinMaxScaler`

### 3.  Model Building
Trained and evaluated the following models:
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier

### 4.  Evaluation Metrics
- Confusion Matrix
- Classification Report (Precision, Recall, F1-score)
- ROC-AUC Score & ROC Curve

### 5.  Hyperparameter Tuning
- Used `GridSearchCV` on Random Forest for optimal parameter selection

---

##  Results

| Model              | Accuracy | Precision | Recall | ROC-AUC |
|-------------------|----------|-----------|--------|---------|
| Logistic Regression | ~88%    | Good      | Good   | Good    |
| Random Forest       | ~90%+   | Better    | Better | Better  |
| XGBoost             | ~90%+   | Best      | Best   | Best    |


** Insights:**\
 Random Forest performed better in terms of recall and AUC-ROC.\
 The marketing campaign success rate is influenced by previous interactions and customer demographics.

---


##  Key Learnings

 Importance of feature engineering in improving model accuracy.\
 How to evaluate models using AUC-ROC & precision-recall metrics.\
 How marketing campaign strategies impact customer decisions.

---

##  Author

**Anirudha Johare**   
📫 [LinkedIn Profile](https://www.linkedin.com/in/anirudhajohare19/)

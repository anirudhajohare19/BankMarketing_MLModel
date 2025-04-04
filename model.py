# import Data Manipulation Libraries
import numpy as np
import pandas as pd

# Import Data Visualization Libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Import Filter Warning Libraries
import warnings
warnings.filterwarnings('ignore')

# Import Logging  Files
import logging

logging.basicConfig(
    level=logging.INFO,
    filemode='w',
    filename='model.log',
    format='%(asctime)s - %(levelname)s - %(message)s',force=True
)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, RocCurveDisplay
import scipy.stats as stats

# Data Import using Pandas Function
url='https://raw.githubusercontent.com/anirudhajohare19/BankMarketing_MLModel/refs/heads/main/BankTelemarketing.csv'

df=pd.read_csv(url,sep=';')

# Split the Dataset into Numerical_Data and Categorical_Data

Numerical_Data=df.select_dtypes(exclude='object')

Categorical_Data=df.select_dtypes(include='object')

# Encoding Target Column
# No : 0 and Yes : 1

df['y']=df['y'].replace({'no':0,'yes':1})

# Encoding default Column
# No : 0 and Yes : 1

df['default']=df['default'].replace({'no':0,'yes':1}) 

# Encoding housing Column
# No : 0 and Yes : 1

df['housing']=df['housing'].replace({'no':0,'yes':1})

# Encoding loan Column
# No : 0 and Yes : 1
df['loan']=df['loan'].replace({'no':0,'yes':1})

# Using Lebel Encoding
from sklearn.preprocessing import LabelEncoder

df['job']=LabelEncoder().fit_transform(df['job'])
df['marital']=LabelEncoder().fit_transform(df['marital'])
df['education']=LabelEncoder().fit_transform(df['education'])
df['contact']=LabelEncoder().fit_transform(df['contact'])
df['month']=LabelEncoder().fit_transform(df['month'])
df['poutcome']=LabelEncoder().fit_transform(df['poutcome'])


X = df.drop(columns='y') 

y=df['y']                


# Step 2: Split The DataSet Into Train and Test
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test= train_test_split(X,y,train_size=0.70,random_state=42)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 4: Using SMOTE Technique to Balance Target Column.
from imblearn.over_sampling import SMOTE
sm = SMOTE(random_state = 42)
X_train, y_train = sm.fit_resample(X_train, y_train)




RF = RandomForestClassifier()

RF.fit(X_train, y_train)

y_predict_RF = RF.predict(X_test)

accuracy_score_RF = accuracy_score(y_test,y_predict_RF)

print("Accuracy:", accuracy_score(y_test, y_predict_RF))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_predict_RF))
print("Classification Report:\n", classification_report(y_test, y_predict_RF))
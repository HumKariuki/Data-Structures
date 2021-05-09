from array import array

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/Statology/Python-Guides/main/default.csv"
data = pd.read_csv(url)

print (data[0:6])
## to show the length of the dataset
print(len(data))

X = data[['student', 'balance', 'income']]
y = data['default']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)
log_regression = LogisticRegression()
log_regression.fit(X_train,y_train)
y_pred= log_regression.predict(X_test)


cnf_matrix = metrics.confusion_matrix(y_test,y_pred)
cnf_matrix

array([[2886,   1],
       [113,    0]])

print("Accuracy:",metrics.accuracy_score(y_test,y_pred))

Accuracy: 0.962


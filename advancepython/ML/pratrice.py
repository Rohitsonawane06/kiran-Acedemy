import pandas as pd
import numpy as np
df=pd.read_csv('student_admission_dataset.csv')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x=df.iloc[:,0:3].values
print(x)

y=df.iloc[:,3].values
print(y)


from sklearn.preprocessing import LabelEncoder
Labelencoder_y=LabelEncoder()
y=Labelencoder_y.fit_transform(y)
print(y)

model=LinearRegression()
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

from sklearn.linear_model import LogisticRegression
logmodel=LogisticRegression()
logmodel.fit(x_train,y_train)

model.fit(x_train,y_train)


user_input=float(input('Enter the CGPA:'))
predicted_score=model.predict([[user_input]])


print(f"Predicted Select or Not:{predicted_score}")

'''
Taks-predict whether a student is admitted to a university or Not
steps-
1]Handle Missing values
2]convert dataset into x and y
3] show prediction using visualization

'''
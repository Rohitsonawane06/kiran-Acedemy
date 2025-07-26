import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import p as plt
# step no 1
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# step 2:
data={'Hours_study':[2,3,4,5,6,7,8,9,10],'Exam_study':[50,60,70,75,70,85,90,92,95]}

# Step 3
df=pd.DataFrame(data)
print(df)
#step 4:
x=df[['Hours_study']]
y=df[['Exam_study']]


# step 5:
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

# step 6 create model using Linerarregression alogorithm
model=LinearRegression()

# step 7:
model.fit(x_train,y_train)

# user input testing

user_input=float(input("enter the number of hourcs study :"))
predicted_score=model.predict([[user_input]])

# printing the output
print(f"Predicted exam score:{predicted_score}")

plt.scatter(x,y,color="green",label="Actual data")
plt.plot(x,model.predict(x),color="blue",label="Predicted data")
plt.xlabel("study Hours")
plt.ylabel("Marks")
plt.legend()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Step 1: Create data
data = {
    'sq_ft': [1000, 1200, 1300, 1500, 1600, 1800, 2000, 2200, 2500],
    'price': [5000000, 5500000, 6800000, 6900000, 7000000, 72000000, 7800000, 8500000, 9200000]
}

# Step 2: Convert to DataFrame
df = pd.DataFrame(data)
print(df)

# Step 3: Split into X (input) and Y (output)
x = df[['sq_ft']]
y = df[['price']]

# Step 4: Train-Test Split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Step 5: Create Model
model = LinearRegression()

# Step 6: Train Model
model.fit(x_train, y_train)

# Step 7: User input and Prediction
user_input = float(input("Enter house size in square feet: "))
predicted_price = model.predict([[user_input]])

# Step 8: Show result
print(f"Predicted House Price: ₹{predicted_price}")

plt.scatter(x,y,color="green",label="Actual data")
plt.plot(x,model.predict (x) ,color="blue",label="Predicted data")
plt.xlabel("sq_ft")
plt.ylabel("price")
plt.legend()
plt.show()


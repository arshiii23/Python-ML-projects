import pandas as pd
from sklearn.linear_model import LinearRegression

# Data
data = {
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 40, 50, 70, 90]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Marks"]

model = LinearRegression()
model.fit(X, y)

#prediction
new_data = pd.DataFrame({"Hours": [6]})
prediction = model.predict(new_data)

print("Predicted Marks:", prediction[0])
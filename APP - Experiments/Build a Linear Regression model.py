# Build a Linear Regression model using Scikit-learn to predict student scores based
# on study hours and evaluate its performance using mean squared error.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv(r"C:\Users\iu\Downloads\score.csv")
X = df[["Hours"]]
y = df["Scores"]

trainx, testx, trainy, testy = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(trainx, trainy)
predicty = model.predict(testx)
mse = mean_squared_error(testy, predicty)

print(f"Mean Squared Error: {mse:.2f}")

plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Linear Regression: Study Hours vs. Exam Score")
plt.legend()
plt.show()

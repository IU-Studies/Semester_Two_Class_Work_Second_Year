import pandas as pd

df = pd.read_csv(r"C:\Users\IU\Downloads\iris.csv")

mean = df["sepal_length"].mean()
print("Mean is:",mean)

mode = df["sepal_length"].mode()
print("Mode is:",mode)

median = df["sepal_length"].median()
print("Median is:",median)

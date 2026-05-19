import pandas as pd

file = pd.read_csv("CSV Analyzer/Telco_Customer_Churn_Dataset .csv")

print(file.head())
print(file.describe())
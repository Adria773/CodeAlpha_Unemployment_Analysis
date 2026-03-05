# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
data = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

# Show first rows
print(data.head())

# Clean Column Names
data.columns = data.columns.str.strip()

# Plot Unemployment Rate
plt.figure(figsize=(10,6))
sns.lineplot(x="Date", y="Estimated Unemployment Rate (%)", data=data)
plt.xticks(rotation=90)
plt.title("Unemployment Rate Trend in India")
plt.show()

# State wise average unemployment
state_avg = data.groupby("Region")["Estimated Unemployment Rate (%)"].mean()

state_avg.plot(kind="bar", figsize=(10,6))
plt.title("Average Unemployment Rate by State")
plt.show()

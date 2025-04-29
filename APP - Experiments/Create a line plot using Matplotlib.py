# Create a line plot using Matplotlib to visualize trends over time in a dataset (e.g.,
# sales data, temperature changes, or stock prices). Include proper labels, titles, and
# legends for the plot.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\iu\Downloads\temp.csv")

df['dt'] = pd.to_datetime(df['dt'])

plt.figure(figsize=(10,6))
plt.plot(df['dt'], df['AverageTemperature'], label='Temperature (°C)', color='tab:blue')
plt.title('Temperature Over Time (Abidjan, Côte D\'Ivoire)', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

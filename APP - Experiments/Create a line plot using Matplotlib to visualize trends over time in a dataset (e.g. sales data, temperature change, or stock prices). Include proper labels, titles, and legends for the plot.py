import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\mayur\Downloads\temp.csv")

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

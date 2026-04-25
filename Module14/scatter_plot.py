from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('avgIQpercountry.csv')

avg_iq_by_continent = df.groupby('Continent')['Average IQ'].mean()

plt.figure(figsize=(10,6))

plt.scatter(df["Mean years of schooling - 2021"], df['Average IQ'],
            color='purple', alpha=0.7)

plt.title('Scatter Plot of Mean Years of Schooling vs. Average IQ')

plt.xlable('Mean years of schooling - 2021')
plt.ylable('Average IQ')

plt.grid(True, linestyle='--', alpha=0.7)

plt.show()

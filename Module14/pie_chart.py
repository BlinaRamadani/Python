from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('avgIQpercountry.csv')

nobel_prizes_by_continent = df.groupby('Continent')['Nobel Prices'].sum()

no_of_continents = nobel_prizes_by_contienent.count()
print(no_of_continents) #Output: 8

color = ['gold','lightcoral','yellow','thistle','orange','lightskyblue','aquamarine','burlywood']
plt.figure(figsize=(10,10))

nobel_prizes_by_continent.plot(kind='pie',colors=colors,autopct='%1.1f%%')
ply.title('Distribution of Nobel Prizes by Continent')

plt.axis('equal')
plt.ylable('')

plt.tight_layout()
plt.show()
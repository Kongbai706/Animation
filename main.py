import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Placeholder: Generate fake rainfall data for 100 years, 12 months per year, 10 cities
np.random.seed(0)
years = np.arange(1925, 2025)
cities = ['CityA', 'CityB', 'CityC', 'CityD', 'CityE', 'CityF', 'CityG', 'CityH', 'CityI', 'CityJ']
months = np.arange(1, 13)
data = []
for year in years:
    for month in months:
        for city in cities:
            rainfall = np.random.uniform(20, 200)  # mm
            lat = np.random.uniform(-60, 60)
            lon = np.random.uniform(-180, 180)
            data.append([year, month, city, lat, lon, rainfall])
df = pd.DataFrame(data, columns=['year', 'month', 'city', 'lat', 'lon', 'rainfall'])

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 5))
sc = ax.scatter([], [], c=[], cmap='Blues', s=50, vmin=20, vmax=200)
ax.set_xlim(-180, 180)
ax.set_ylim(-60, 60)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Monthly Average Rainfall (1925-2024)')
cb = plt.colorbar(sc, ax=ax, label='Rainfall (mm)')

# Animation function
def animate(i):
    year = years[i // 12]
    month = months[i % 12]
    subset = df[(df['year'] == year) & (df['month'] == month)]
    sc.set_offsets(subset[['lon', 'lat']].values)
    sc.set_array(subset['rainfall'].values)
    ax.set_title(f'Monthly Average Rainfall: {year}-{month:02d}')
    return sc,

ani = animation.FuncAnimation(fig, animate, frames=len(years)*12, interval=100, blit=True)
plt.show()

import pandas as pd
import folium

data = pd.read_csv('mental_hospitals.csv')

m = folium.Map(location=[36.5, 127.5], zoom_start=7)

for idx, row in data.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row['Name'],
    ).add_to(m)

m.save('mental_hospitals_map.html')

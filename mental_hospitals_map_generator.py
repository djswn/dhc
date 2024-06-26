import pandas as pd
import folium

# CSV 파일을 읽어옵니다. (파일 경로를 지정해야 합니다)
data = pd.read_csv('mental_hospitals.csv')

# 지도의 초기 위치를 설정합니다 (대한민국 중심부의 좌표를 사용합니다)
m = folium.Map(location=[36.5, 127.5], zoom_start=7)

# 데이터프레임의 각 행을 순회하면서 마커를 추가합니다
for idx, row in data.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row['Name'],
    ).add_to(m)

# 지도를 HTML 파일로 저장합니다
m.save('mental_hospitals_map.html')

import pandas as pd
import folium
from folium import Map, Marker, Tooltip

df = pd.read_csv('study_sites.csv', sep=';')

# token = open("mapbox_token.txt").read()
paleo_map = Map(location=[4.740165, -73.980105], tiles='CartoDB positron', zoom_start=6)

for index, row in df.iterrows():
    researcher = row['Researcher']
    site = row['Site']
    print(researcher, site)
    Marker([row['Latitude'], row['Longitude']], tooltip=Tooltip(f'<p><b>{researcher}</b></p> <br> <p><b>{site}</b></p>',)).add_to(paleo_map)

paleo_map.save('index.html')
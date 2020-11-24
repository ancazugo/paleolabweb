import base64
import pandas as pd
import folium
from folium import Map, Marker, TileLayer, Tooltip, Popup, Icon, IFrame, Html

df = pd.read_csv('study_sites.csv', sep=';')

basemaps = {
    'Google Satellite': TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Satellite',
        overlay = False,
        control = True,
        show=False
    ),
    'Google Terrain': TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Terrain',
        overlay = False,
        control = True,
        show=False
    )
}

# token = open("mapbox_token.txt").read()
paleo_map = Map(location=[4.740165, -73.980105], tiles=None, zoom_start=5)

for index, row in df.iterrows():
    site = str(row['Site']).encode().decode('UTF-8')
    description = str(row['Description']).encode().decode('UTF-8')
#     image = row['Image']
    image = 'images/verjon.jpg'
    encoded = base64.b64encode(open(image, 'rb').read())

    html_popup="""
    <h2>{}</h2>
    <p>{}</p>
    <img src="data:image/png;base64,{}" width='350'>
    """.format
    
    iframe = IFrame(html_popup(site, description,encoded.decode('UTF-8')), width=400, height=400)
    popup = Popup(iframe, max_width=2650)
    
    html_tooltip = """
    <h4>{}</h4>
    <p>Click for more</p>
    """.format
    
    tooltip = Tooltip(html_tooltip(site.encode('unicode_escape').decode('UTF-8')))
        
    Marker([row['Latitude'], row['Longitude']], tooltip=tooltip, popup=popup, icon=Icon(color='darkgreen', icon='leaf')).add_to(paleo_map)
    
TileLayer('Stamen Watercolor', name='Stamen Watercolor', overlay=False, show=True).add_to(paleo_map)
TileLayer('Stamen Terrain', name='Stamen Terrain', overlay=False, show=False).add_to(paleo_map)
basemaps['Google Terrain'].add_to(paleo_map)
basemaps['Google Satellite'].add_to(paleo_map)

folium.LayerControl().add_to(paleo_map)

paleo_map.save('index.html')
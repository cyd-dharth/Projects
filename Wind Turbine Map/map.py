import folium
import pandas as pd

wt = pd.read_excel('wind_turbine.xlsx')
lon = list(wt['long'])
lat = list(wt['lati'])
nam = list(wt['p_name'])
capi = list(wt['p_cap'])


def capacity(cap):
    if cap < 50:
        return 'red'
    elif cap < 150:
        return 'orange'
    elif cap < 500:
        return 'green'
    else:
        return 'blue'


map1 = folium.Map(location=[42.51921492375557, -103.28750005576161], zoom_start=4, tiles='stamen terrain')
'''map1.add_child(folium.Marker(location=[26.505531918298544, 80.22645285135191], popup='Hall X (Lala) Canteen',
                             icon=folium.Icon(color='green')))'''
# ---------------OR -----------------

fg = folium.FeatureGroup('my_map')

for ln, lt, n, cap in zip(lat, lon, nam, capi):
    fg.add_child(
        folium.CircleMarker(location=[ln, lt], popup=str(n), radius=5, fill_color=capacity(cap), color='grey', fill_capacity=0.7))

map1.add_child(fg)
map1.add_child(folium.LayerControl())
map1.save('new2.html')

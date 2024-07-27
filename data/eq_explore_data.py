import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
filename = "data/all_hour.geojson"
mags,lons,lats = [],[],[]
with open(filename) as f:
    all_eq_data = json.load(f)
    all_eq_dict = all_eq_data['features']
    for x in all_eq_dict:
        mag = x["properties"]['mag']
        mags.append(mag)
        lon = x['geometry']['coordinates'][0]
        lat = x['geometry']['coordinates'][1]
        lons.append(lon)
        lats.append(lat)
data = [Scattergeo(lon=lons, lat=lats,fillcolor='red',marker={'size' : [5*mag for mag in mags],'color':mags,'colorscale':'solar','reversescale':True,'colorbar': {'title': 'Magnitude'}})]
my_layout = Layout(title='Global Earthquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
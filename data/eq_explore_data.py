import json
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
    print(mags)
    print(lats)
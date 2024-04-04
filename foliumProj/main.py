import numpy as np
import pandas as pd
import folium
import csv



footprints = pd.read_csv("foliumProj/data.csv")
political_countries_url = (
    "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
)
m = folium.Map(location=[56.130, -106.35], zoom_start=4, tiles="cartodb positron")

folium.GeoJson(political_countries_url).add_to(m)

# sets the map for the project, world map configure to make it canada only
m.save("CanExportImport.html")

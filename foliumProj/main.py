import numpy as np
import pandas as pd
import folium
from folium import Choropleth, GeoJson, LayerControl
import csv
import math
from folium import plugins



# Used a coordinate based GeoJSON file to actually map out the province borders
# Will implement chloropleth to visualize data better

file_path = 'foliumProj/dataset/s2020pv_e.xls'

try:
    # df is dataframe for Folium
    df = pd.read_excel(file_path, engine='xlrd')
    print(df.head())  
    # just to show the first few rows to confirm its active
except Exception as e:
    print(f"An error occurred: {e}")

# sums up all the values by province
provinceTotals = df.groupby('Province').agg({'Total Canada': 'sum'}).reset_index()

#geoJson file to populate the province boundaries
provinceTotals.rename(columns={'Province': 'Province_Name', 'Total Canada': 'Value'}, inplace=True)

# Read the GeoJSON file (assuming you have the correct path)
geojson_file_path = 'foliumProj/dataset/georef-canada-province@public.geojson'
with open(geojson_file_path, 'r') as f:
    geojson_data = f.read()

# Initialize the map centered around Canada
m = folium.Map(location=[56.130, -106.35], zoom_start=4, tiles="cartodb positron")

# creating mini map feature
minimap = plugins.MiniMap()
m.add_child(minimap)
m
# Create a Choropleth layer
folium.Choropleth(
    geo_data=geojson_data,
    name='choropleth',
    data=provinceTotals,
    columns=['Province_Name', 'Value'],
    key_on='feature.properties.prov_name_en',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Commercial Value (thousand dollars)'
).add_to(m)

# Add layer control to toggle the choropleth
LayerControl().add_to(m)

# sets the map for the project, world map configure to make it canada only
m.save("CanExportImport.html")
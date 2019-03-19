#py pip install folium  (Instalacipon de mapas para python)
import folium
import numpy as np
import pandas as pd

data= pd.read_csv("C:/Users/admin/Documents/Fanny Mayorga/Python/csv/Indicators.csv")

hist_indicator = 'CO2 emissions \(metric' 
hist_year = 2011

mask1 = data['IndicatorName'].str.contains(hist_indicator) 
mask2 = data['Year'].isin([hist_year]) 

stage = data[mask1 & mask2]

plot_data = stage[['CountryCode','Value']]

hist_indicator = stage.iloc[0]['IndicatorName']

map = folium.Map(location=[100,0], zoom_start=1.5)

map.choropleth(geo_path=contry_geo,data=plot_data,
                columns=['CountryCode','Value'],
                fill_color='YlGnBu',fill_opacity=0.7,line_opacity=0.2,
                legend_name=hist_indicator)

print(plot_data.head())

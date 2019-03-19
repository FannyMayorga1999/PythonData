import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#git lfs migrate import --include="*.csv" para incluir archico demasiado grandes


data= pd.read_csv("C:/Users/admin/Documents/Fanny Mayorga/Python/csv/Indicators.csv")

hist_indicator = 'GDP per capita \(constant 2005' 
hist_indicator01 = 'CO2 emissions \(metric' 
hist_year = 2011 
hist_country = 'USA'                                  

mask1 = data['IndicatorName'].str.contains(hist_indicator) 
mask2 = data['CountryCode'].str.contains(hist_country)
mask3 = data['IndicatorName'].str.contains(hist_indicator01)
mask4 = data['CountryCode'].str.contains(hist_country)

gdp_stage = data[mask1 & mask2]
stage = data[mask4 & mask3]

print(stage.head())

plt.plot(gdp_stage['Year'].values, gdp_stage['Value'].values)

plt.xlabel('Years')
plt.ylabel(gdp_stage['IndicatorName'].iloc[0])
plt.title('GPA per Capita Usa')

"""
gdp_stage_trunc = gdp_stage[gdp_stage['Year']<2012]

fig, axis =plt.subplots(2, 1)

axis.yaxis.grid(True)
axis.set_title('CO2 Emissions vs. GDP \(per capita\)', fontsize=10)
axis.set_xlabel(gdp_stage_trunc['IndicatorName'].iloc[0],fontsize=10)
axis.set_ylabel(stage['IndicatorName'].iloc[0],fontsize=10)


X = gdp_stage_trunc['Value']
Y = stage['Value']

axis.scatter(X,Y)

#print(gdp_stage_trunc)"""
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#git lfs migrate import --include="*.csv" para incluir archico demasiado grandes


data= pd.read_csv("C:/Users/admin/Documents/Fanny Mayorga/Python/csv/Indicators.csv")

hist_indicator = 'CO2 emissions \(metric' 
hist_year = 2011 
hist_country = 'USA'                                  

mask1 = data['IndicatorName'].str.contains(hist_indicator) 
mask2 = data['CountryCode'].str.contains(hist_country) 

mask3 = data['Year'].isin([hist_year])                              #buscada con numeros

stage = data[mask1 & mask2]
CO2_2011 = data[mask1 & mask3]


years = stage['Year'].values
co2 = stage['Value'].values

print(years)

plt.bar(stage['Year'].values, stage['Value'].values)
plt.xlabel('Years')
plt.ylabel(stage['IndicatorName'].iloc[0])
plt.title('CO2 Emissions in USA')

#---------------------------------------------------------------------------------------------------------
#segundo grafico

fig, ax = plt.subplots()
ax.annotate("USA",
            xy =(18,5), xycoords = 'data',
            xytext=(18,30), textcoords = 'data',
            arrowprops = dict(arrowstyle="->",
                                connectionstyle="arc3"),
            )

plt.hist(CO2_2011['Value'],10,normed=False, facecolor='red')
plt.xlabel(stage['IndicatorName'].iloc[0])
plt.ylabel('# of Countries')
plt.title('Histogram od CO2 Emissions Per Capital')
 
plt.grid(True)
plt.show()

#print(stage.head())


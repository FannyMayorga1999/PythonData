from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import utils           
import pandas as pd
import numpy as np 
from itertools import cycle, islice
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

data = pd.read_csv("C:/Users/admin/Documents/Fanny Mayorga/Python/csv/queue_calls.csv")

print(data.shape)

"""
data['time'] = pd.to_datetime(data['time']) 
data['holdtime'] = pd.to_datetime(data['holdtime'])
data['calltime'] = pd.to_datetime(data['calltime'])
"""
"""

data['time'] = data['time'].astype(np.int64)
data['holdtime'] = data['holdtime'].astype(np.int64)
data['calltime'] = data['calltime'].astype(np.int64)
"""
import pandas as pd
import matplotlib.pyplot as plt

climate = pd.read_csv('daily_climate.csv')
print(climate.columns.tolist())

# Rename columns to be used for graph
climate = climate.rename(columns = {
    'Max Temp (°C)' : 'max_temp',
    'Date/Time' : 'date'
})

# Grab first 15 temperature data points for y-axis 
y_axis = climate.loc[0:15, 'max_temp']
# Grab first 15 time data points for x-axis 
x_axis = climate.loc[0:15, 'date']

#def create_graph(x,y)
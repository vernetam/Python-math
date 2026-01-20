import pandas as pd
import matplotlib.pyplot as plt

alg_park_climate = pd.read_csv('algonquin_park_west_temp.csv')
big_chute_climate = pd.read_csv('big_chute_temp.csv')
# Code to see column names
#print(alg_park_climate.columns.tolist())

# Rename columns to be used for graph
alg_park_climate = alg_park_climate.rename(columns = {
    'Max Temp (°C)' : 'max_temp',
    'Date/Time' : 'date'
})
big_chute_climate = big_chute_climate.rename(columns = {
    'Max Temp (°C)' : 'max_temp',
    'Date/Time' : 'date'
})

# Grab first 15 temperature data points for y-axis 
alg_y_axis = alg_park_climate.loc[0:10, 'max_temp']
bigchute_y_axis = big_chute_climate.loc[0:10, 'max_temp']
# Grab first 15 time data points for x-axis 
alg_x_axis = alg_park_climate.loc[0:10, 'date']
bigchute_x_axis = big_chute_climate.loc[0:10, 'date']

def create_graph(x1,y1,x2,y2):
    plt.plot(x1,y1,x2,y2)
    plt.title('Max January Temp')
    plt.legend(['Algonquin Park West', 'Big Chute'])
    plt.xlabel('Date')
    plt.ylabel('Temperature (centigrade)')
    plt.show()

if __name__ == '__main__':
    create_graph(alg_x_axis,alg_y_axis,bigchute_x_axis,bigchute_y_axis)
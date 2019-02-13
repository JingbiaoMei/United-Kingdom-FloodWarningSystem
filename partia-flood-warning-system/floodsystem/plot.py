import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
from floodsystem.analysis import polyfit
import matplotlib


def plot_water_levels(station, dates, levels): 
    # Plot
    plt.plot(dates, levels)
    level_max = max(levels)
    date_max =  dates[levels.index(level_max)]
    level_min = min(levels)
    date_min =  dates[levels.index(level_min)]
    plt.annotate("Max",(date_max, level_max))
    plt.annotate("Min",(date_min, level_min))
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()  

def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)
    x1 = np.linspace(x[0], x[-1], 50)
    plt.plot(x1, poly(x1 - x[0]))
    plot_water_levels(station, dates, levels)
    
   

 
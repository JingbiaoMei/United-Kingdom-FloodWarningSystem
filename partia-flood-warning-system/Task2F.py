from floodsystem.plot import plot_water_level_with_fit 
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
import numpy as np
def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    #Initiate empty list
    levellist = []

    #initiate temperory storage for water level data for error processing
    templevel = 0

    # iterate for all stations
    for station in stations:
        templevel = station.latest_level
        # Change NonType to zero for data analysis
        if templevel == None:
            templevel = 0
        # Change negative error data to zero
        if templevel < 0:
            templevel = 0 
        # append to a list
        levellist.append((station.name,templevel))
    
    # Sorted after iteration    
    levellist = sorted_by_key(levellist,1)
    # get the greatest five station
    levellist = levellist[-5:]
    # Get the name of the 5 stations (first entry of the tumple)
    stationname = []
    for llist in levellist:
        stationname.append(llist[0])
    print(stationname)

    for station_name in stationname:    
        station_temp = None
        for station in stations:
            if station.name == station_name:
                station_temp = station
                break
        dt = 12
        dates, levels = fetch_measure_levels(station_temp.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(station_name, dates, levels, 4)




if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()

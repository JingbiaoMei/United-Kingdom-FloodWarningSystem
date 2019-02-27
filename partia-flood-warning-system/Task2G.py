import floodsystem.flood
import floodsystem.stationdata

def run():
    #Test sample of some station
    stations = floodsystem.stationdata.build_station_list()
    # Get the Total Number of Stations
    totalNum = len(stations)
    # Use Normal Distribution 
    flood_Risk_Num = int(0.025 * totalNum)
    print(flood_Risk_Num)
    floodsystem.stationdata.update_water_levels(stations)
    # Running the function to get a list called result
    result = floodsystem.flood.stations_highest_rel_level(stations, flood_Risk_Num)
    # Printing the result with 4 levels
    for x in range (len(result)):
        if x <= 0.25 * len(result):
            print(result[x][0], " Severe")
        elif x <= 0.50 * len(result):
            print(result[x][0], " High")
        elif x <= 0.75 * len(result):  
            print(result[x][0], " Moderate")
        else:
            print(result[x][0], " Low")

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
import floodsystem.flood
import floodsystem.stationdata

def run():
    #Test sample of some station
    stations = floodsystem.stationdata.build_station_list()
    floodsystem.stationdata.update_water_levels(stations)
    # Running the function to get a list called result
    result = floodsystem.flood.stations_highest_rel_level(stations, 10)
    # Printing the result
    for x in range (len(result)):
        print(result[x][0], result[x][1])

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
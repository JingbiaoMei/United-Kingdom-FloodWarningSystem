import floodsystem.flood
import floodsystem.stationdata

def run():

    # Test sample of some station
    stations = floodsystem.stationdata.build_station_list()
    floodsystem.stationdata.update_water_levels(stations)

    # Running the function to get a list called result
    result = floodsystem.flood.stations_level_over_threshold(stations, 0.8)

    # Loop to print the output as shown
    for x in range (len(result)):
        # Printing the result
        print(result[x][0].name, result[x][1])

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()



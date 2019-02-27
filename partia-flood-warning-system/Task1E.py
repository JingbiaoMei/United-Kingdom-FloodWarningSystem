from floodsystem.geo import rivers_by_station_number

from floodsystem.stationdata import build_station_list

def run():
    #Test sample of some station
    stations = build_station_list()
    # Running the function to get a list called result
    result = rivers_by_station_number(stations,6)
    # Printing the result
    print(result)


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()

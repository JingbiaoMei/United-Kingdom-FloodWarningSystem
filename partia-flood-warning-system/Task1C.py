from floodsystem.geo import stations_within_radius

from floodsystem.stationdata import build_station_list

def run():
    #Test sample of some station
    stations = build_station_list()
    # Running the function to get a list called result
    result = stations_within_radius(stations,(52.2053, 0.1218),10)
    # Printing the result
    print(result)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()

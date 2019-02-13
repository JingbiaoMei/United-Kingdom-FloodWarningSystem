



import floodsystem
from floodsystem.stationdata import build_station_list
def run():
    #Test sample of some station
    stations = build_station_list()
    # Running the function to get a list called result
    result = floodsystem.station.MonitoringStation.inconsistent_typical_range_stations(stations)
    # Printing the result
    print(result)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
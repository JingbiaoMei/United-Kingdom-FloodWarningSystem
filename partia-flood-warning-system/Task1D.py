from floodsystem.geo import rivers_with_station

from floodsystem.geo import stations_by_river

from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1A"""
    stations = build_station_list() # Get Stations 
    riverset = rivers_with_station(stations) # get a set of all rivers 
    print(len(riverset)) # get number of rivers
    riverlist = list(riverset)  # transfer the set to a list to get first 10 items
    riverlist = sorted(riverlist) # sort the list alphabatically
    print(riverlist[:10]) # print first 10

    dictionary = stations_by_river(stations) # get the dictionary which maps the stationa by rivers
    print(dictionary['River Aire']) #print
    print(dictionary['River Cam'])
    print(dictionary['River Thames'])

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
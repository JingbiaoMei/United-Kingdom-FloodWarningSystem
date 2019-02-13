from floodsystem.geo import stations_by_distance_with_town

from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list() # Get Stations 
    listA = stations_by_distance_with_town(stations,(52.2053, 0.1218)) # Sorted by distance
    closeTen = listA[:10] # Get top 10
    farTen = listA[-10:] # Get Furthest 10
    
    def reformat(anylist): # reformat the tuple inside the list to look the same as we want
        newlist = []
        for i in range(10):
            newlist.append((anylist[i][0][0],anylist[i][0][1],anylist[i][1])) #Break the tuple inside tuple into one tuple of three figures 
        return newlist
    print(reformat(closeTen))
    print(reformat(farTen))

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
import floodsystem.stationdata
import floodsystem.flood


def test_stations_level_threshold():

    stations = floodsystem.stationdata.build_station_list()
    floodsystem.stationdata.update_water_levels(stations)

    N = 0.1

    while N < 1:

        result = floodsystem.flood.stations_level_over_threshold(stations, N)
        assert isinstance(result, list)

        for x in range (len(result)-1):
            assert(float(result[x][1])>=float(result[x+1][1]))
        N = N + 0.0001

test_stations_level_threshold()



def test_stations_highest_rel_level():

    stations = floodsystem.stationdata.build_station_list()
    floodsystem.stationdata.update_water_levels(stations)

    N = 1

    while N < 10000:

        result = floodsystem.flood.stations_highest_rel_level(stations, N)

        assert isinstance(result, list)



        for x in range (len(result)-1):
            assert(float(result[x][1])>=float(result[x+1][1]))

        N = N+1

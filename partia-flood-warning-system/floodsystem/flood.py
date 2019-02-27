import floodsystem.station




def stations_level_over_threshold(stations, tol):
    """
        function that returns a list of tuples, where each tuple holds
        (i) a station (object) at which the latest relative water level is over tol
        (ii) the relative water level at the station.
    """
    temp = []

    for station in stations:

        val = station.relative_water_level()
        if val is not None:
            if val > tol:
                temp.append((station, val))

    templist = sorted(temp, key = lambda temp: temp[1], reverse = True)


    return templist

def stations_highest_rel_level(stations, N):
    """"
        function in the submodule flood that returns a list of the N stations (objects) at which the water level, relative to the typical range, is highest.
    """


    num = 0
    temp = []
    slist = []

    for station in stations:

        val = station.relative_water_level()

        if val is not None:
            temp.append([station, val])

    templist = sorted(temp, key = lambda temp: temp[1], reverse = True)

    while num < N and num < len(templist):
        slist.append([templist[num][0].name,templist[num][1]])
        num += 1

    return slist





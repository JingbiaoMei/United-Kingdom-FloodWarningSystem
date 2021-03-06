# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord

        self.typical_range = typical_range

        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """Compares that lower limit is less than higher limit"""
        typical_range = self.typical_range  # Retrieving the typical_range
        if typical_range is not None:  # Ensuring it is not None
            if typical_range[0] < typical_range[1]:  # Checking if first number is lower than second number
                return True
            else:
                return False
        else:
            return False

    def inconsistent_typical_range_stations(stations):
        """Find the list of stations in alphabetical order with inconsistent typical ranges"""
        slist = []
        # Loop to check if a station's typical ranage is consistent
        for station in stations:
            if MonitoringStation.typical_range_consistent(station) == False:
                slist.append(station.name)      #Add the station to the return list


        slist.sort()    # Sorting the list in alphabetical order



        return slist

    def relative_water_level(self):
        """
            returns the latest water level as a fraction of the typical range

        """

        currLevel= self.latest_level

        bool = self.typical_range_consistent()

        if bool == True:
            typical_high = self.typical_range[1]
            typical_low = self.typical_range[0]

        if currLevel is None or bool == False:
            return None

        else:
            result = ((currLevel-typical_low)/(typical_high-typical_low))

        return result
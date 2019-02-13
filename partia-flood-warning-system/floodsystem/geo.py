# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.


"""

import numpy as np

from haversine import haversine
 # distance between two geographic coordinates 

from floodsystem.utils import sorted_by_key

def stations_by_distance(stations, p):
    """Function to sort stations distance from a coordinate"""
    sdlist = [] # List store all the station and distance with p
    distance = 0
    for station in stations: # Loop for all the stations
        cord = station.coord # Coordinate of the station
        distance = haversine(p,cord) # Use function to get the distance
        sdlist.append((station.name,distance)) # Add  Tuple to the List
    return sorted_by_key(sdlist,1) # Return the sorted list

def stations_by_distance_with_town(stations, p): 
    """function for doing 1B demonstration program"""
    sdlist = [] # List store all the station and distance with p
    distance = 0
    for station in stations: # Loop for all the stations
        cord = station.coord # Coordinate of the station
        distance = haversine(p,cord) # Use function to get the distance
        town = station.town
        sdlist.append(((station.name,town),distance)) # Add  Tuple to the List
    return sorted_by_key(sdlist,1) # Return the sorted list

def stations_within_radius(stations, centre, r):
    """Helps identify stations with the specified radius"""
    if stations is not None and centre is not None and r >0:
        slist = []  # List that will be returned
        c_lat = centre[0]  # latitude coordinate of center
        c_long = centre[1]  # longitude coordinate of center

        for station in stations:  # Loop to check all the stations

            coord = station.coord  # Coordinate of the stations
            pos_lat = coord[0]  # X coordinate of station
            pos_long = coord[1]  # Y coordinate of station
            det_lat = np.radians(pos_lat-c_lat)
            det_long = np.radians(pos_long-c_long)

            a = np.power(np.sin(det_lat/2),2) + (np.cos(np.radians(pos_lat))*np.cos(np.radians(c_lat))*np.power(np.sin(det_long/2),2))
            c = 2*np.arctan2(np.power(a,0.5), np.power((1-a),0.5))

            radius = 6371*c  # distance between the two coordinates
            if r > radius:  # if the distance is less than radius then it lies in the circle
                slist.append(station.name)  # Adding the station to the list
        return slist  # returning the list

    else:
        print("Please check if input parameters are not Null values")

def rivers_with_station(stations):
    """Function to get all the river monitored in a set"""
    riverset = set() # river set
    for station in stations:
        riverset.add(station.river)
    return riverset

def stations_by_river(stations):
    """Function to get a dictionary that maps stations by river"""
    riverDictionary = {} # get an empty set of dictionary for rivers 
    riverList = list(rivers_with_station(stations)) # transfer sets to a list of stations
    for river in riverList: # outside for loop for river
        temp = [] #initiate temporary list for all station names on a river
        for station in stations: # inside loop iterate for all stations
            if river == station.river: # check if the river matches the one we wants
                temp.append(station.name) # if true added to the temporary list
        temp = sorted(temp) # sorted the temporary list
        riverDictionary.update({river : temp}) # Update the dictionary
    return riverDictionary

def rivers_by_station_number(stations, N):
    """Gives N rivers with maximum station and rivers with same no of stations are counted as one"""
    dictionary = {}       # A dictionary will store how many rivers have how many stations
    slist = []      # List to be returned
    unique_river = set() # store the unique rivers - to not get an error - adding a new key to dic

    for station in stations:    # Loop to check all the stations
        river = station.river   # Get the river name

        if river in unique_river:   # Check if river in the set
            dictionary[river] += 1      # Increasing Frequency

        else:
            unique_river.add(river)
            dictionary[river] = 1       # Increasing Frequency

    sorted_list = sorted((dictionary.items()), key=lambda dictionary: dictionary[1], reverse=True)  # Sorting the dic val in reverse

    sorted_list = [tuple(item) for item in sorted_list]  # Converting to request return type

    val_max = sorted_list[0][1]  # River with maximum station

# Loop to append the N- largest rivers in the return list

    num = 0
    i = 1
    slist.append(sorted_list[0])

    while num < N and i < len(sorted_list):
        
        val = sorted_list[i][1]
        

        if val == val_max:
            slist.append(sorted_list[i])
            break

        slist.append(sorted_list[i])
        num +=1    
        i=i+1
    return slist


# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)




    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistency():
    """"Testing the range consistency"""
    # Create a list of stations for testing
    stations = []

    s_id0 = "test-s-idA"
    m_id0 = "test-m-idA"
    label0 = "Station A"
    coord0 = (52.204451, 0.119726)
    trange0 = (22.3, 3.4445)
    river0 = "River A"
    town0 = "Town A"
    s0 = MonitoringStation(s_id0, m_id0, label0, coord0, trange0, river0, town0)

    stations.append(s0)

    s_id1 = "test-s-idB"
    m_id1 = "test-m-idB"
    label1 = "Station B"
    coord1 = (52.265989, 0.119921)
    trange1 = (32.3, 3.4445)
    river1 = "River B"
    town1 = "Town B"
    s1 = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)

    stations.append(s1)

    s_id2 = "test-s-idC"
    m_id2 = "test-m-idC"
    label2 = "Station C"
    coord2 = (52.519327, 1.016386)
    trange2 = (-2.3, 3.4445)
    river2 = "River C"
    town2 = "Town C"
    s2 = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)

    stations.append(s2)

    s_id3 = "test-s-idD"
    m_id3 = "test-m-idD"
    label3 = "Station D"
    coord3 = (52.632525, 1.295940)
    trange3 = (-2.3, 3.4445)
    river3 = "River D"
    town3 = "Town D"
    s3 = MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)

    stations.append(s3)

    s_id4 = "test-s-idE"
    m_id4 = "test-m-idE"
    label4 = "Station E"
    coord4 = (52.454529, 5.525467)
    trange4 = None
    river4 = "River E"
    town4 = "Town E"
    s4 = MonitoringStation(s_id4, m_id4, label4, coord4, trange4, river4, town4)

    stations.append(s4)

    result1 = MonitoringStation.inconsistent_typical_range_stations(stations)
    print(result1)

    assert result1 == ['Station A', 'Station B', 'Station E']

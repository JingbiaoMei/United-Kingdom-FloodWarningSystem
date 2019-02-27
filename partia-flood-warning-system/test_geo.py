from floodsystem.station import MonitoringStation

import floodsystem.geo

def test_stations_by_distance():
    """Testing for sorting by distance"""
    stations = []
    
    s_id0 = "test-s-idA"
    m_id0 = "test-m-idA"
    label0 = "StationA"
    coord0 = (0, 0)
    trange0 = (-2.3, 3.4445)
    river0 = "River A"
    town0 = "Town A"
    s0 = MonitoringStation(s_id0, m_id0, label0, coord0, trange0, river0, town0)

    stations.append(s0)

    s_id1 = "test-s-idB"
    m_id1 = "test-m-idB"
    label1 = "Station B"
    coord1 = (50, 50)
    trange1 = (-2.3, 3.4445)
    river1 = "River B"
    town1 = "Town B"
    s1 = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)

    stations.append(s1)

    s_id2 = "test-s-idC"
    m_id2 = "test-m-idC"
    label2 = "Station C"
    coord2 = (100, 100)
    trange2 = (-2.3, 3.4445)
    river2 = "River C"
    town2 = "Town C"
    s2 = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)

    stations.append(s2)
    result1 = floodsystem.geo.stations_by_distance(stations,(1,1))
    assert result1 == [('StationA', 157.2495984740402), ('Station B', 7140.276572656417), ('Station C', 9724.92501810167)]
    result2 = floodsystem.geo.stations_by_distance(stations,(50,50))
    assert result2 == [('Station B', 0.0), ('Station C', 5220.409050705932), ('StationA', 7293.897181472728)]

test_stations_by_distance()

def test_station_within_radius():
    """Testing for radius command"""

    stations = []

    s_id0 = "test-s-idA"
    m_id0 = "test-m-idA"
    label0 = "StationA"
    coord0 = (52.204451, 0.119726)
    trange0 = (-2.3, 3.4445)
    river0 = "River A"
    town0 = "Town A"
    s0 = MonitoringStation(s_id0, m_id0, label0, coord0, trange0, river0, town0)

    stations.append(s0)

    s_id1 = "test-s-idB"
    m_id1 = "test-m-idB"
    label1 = "Station B"
    coord1 = (52.265989, 0.119921)
    trange1 = (-2.3, 3.4445)
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
    trange4 = (-2.3, 3.4445)
    river4 = "River E"
    town4 = "Town E"
    s4 = MonitoringStation(s_id4, m_id4, label4, coord4, trange4, river4, town4)

    stations.append(s4)



    result1 = floodsystem.geo.stations_within_radius(stations, (52.198962, 0.119877), 5)
    result2 = floodsystem.geo.stations_within_radius(stations, (52.198962, 0.119877), 10)
    result3 = floodsystem.geo.stations_within_radius(stations, (52.198962, 0.119877), 80)
    result4 = floodsystem.geo.stations_within_radius(stations, (52.198962, 0.119877), 100)
    result5 = floodsystem.geo.stations_within_radius(stations, (52.198962, 0.119877), 500)

    assert result1 == [s0.name]
    assert result2 == [s0.name,s1.name]
    assert result3 == [s0.name,s1.name,s2.name]
    assert result4 == [s0.name,s1.name,s2.name,s3.name]
    assert result5 == [s0.name,s1.name,s2.name,s3.name,s4.name]




test_station_within_radius()


def test_rivers_by_station_number():
    """Testing for rivers with maximum stations"""
    stations = []

    s_id0 = "test-s-idA"
    m_id0 = "test-m-idA"
    label0 = "StationA"
    coord0 = (52.204451, 0.119726)
    trange0 = (-2.3, 3.4445)
    river0 = "River A"
    town0 = "Town A"
    s0 = MonitoringStation(s_id0, m_id0, label0, coord0, trange0, river0, town0)

    stations.append(s0)

    s_id1 = "test-s-idB"
    m_id1 = "test-m-idB"
    label1 = "Station B"
    coord1 = (52.265989, 0.119921)
    trange1 = (-2.3, 3.4445)
    river1 = "River B"
    town1 = "Town B"
    s1 = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)

    stations.append(s1)

    s_id2 = "test-s-idC"
    m_id2 = "test-m-idC"
    label2 = "Station C"
    coord2 = (52.519327, 1.016386)
    trange2 = (-2.3, 3.4445)
    river2 = "River B"
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
    trange4 = (-2.3, 3.4445)
    river4 = "River B"
    town4 = "Town E"
    s4 = MonitoringStation(s_id4, m_id4, label4, coord4, trange4, river4, town4)

    stations.append(s4)

    s_id5 = "test-s-idE"
    m_id5 = "test-m-idE"
    label5 = "Station E"
    coord5 = (52.454529, 5.525467)
    trange5 = (-2.3, 3.4445)
    river5 = "River A"
    town5 = "Town E"
    s5 = MonitoringStation(s_id5, m_id5, label5, coord5, trange5, river5, town5)

    stations.append(s5)

    s_id6 = "test-s-idE"
    m_id6 = "test-m-idE"
    label6 = "Station E"
    coord6 = (52.454529, 5.525467)
    trange6 = (-2.3, 3.4445)
    river6 = "River D"
    town6 = "Town E"
    s6 = MonitoringStation(s_id6, m_id6, label6, coord6, trange6, river6, town6)

    stations.append(s6)

    s_id7 = "test-s-idE"
    m_id7 = "test-m-idE"
    label7 = "Station E"
    coord7 = (52.454529, 5.525467)
    trange7 = (-2.3, 3.4445)
    river7 = "River D"
    town7 = "Town E"
    s7 = MonitoringStation(s_id7, m_id7, label7, coord7, trange7, river7, town7)

    stations.append(s7)

    s_id8 = "test-s-idE"
    m_id8 = "test-m-idE"
    label8 = "Station E"
    coord8 = (52.454529, 5.525467)
    trange8 = (-2.3, 3.4445)
    river8 = "River E"
    town8 = "Town E"
    s8 = MonitoringStation(s_id8, m_id8, label8, coord8, trange8, river8, town8)

    stations.append(s8)

    result1 = floodsystem.geo.rivers_by_station_number(stations,1)
    result2 = floodsystem.geo.rivers_by_station_number(stations, 2)
    result3 = floodsystem.geo.rivers_by_station_number(stations, 3)
    result4 = floodsystem.geo.rivers_by_station_number(stations, 4)
    result5 = floodsystem.geo.rivers_by_station_number(stations, 5)



    assert result1 == [('River B', 3),('River D', 3)]
    assert result2 == [('River B', 3), ('River D', 3)]
    assert result3 == [('River B', 3), ('River D', 3), ('River A', 2)]
    assert result4 == [('River B', 3), ('River D', 3), ('River A', 2), ('River E', 1)]
    assert result5 == [('River B', 3), ('River D', 3), ('River A', 2), ('River E', 1)]



test_rivers_by_station_number()

def test_stations_by_river():       
    """Testing for stations mapped by river"""
    stations = []
    s_id0 = "test-s-idA"
    m_id0 = "test-m-idA"
    label0 = "Station A"
    coord0 = (52.204451, 0.119726)
    trange0 = (-2.3, 3.4445)
    river0 = "River A"
    town0 = "Town A"
    s0 = MonitoringStation(s_id0, m_id0, label0, coord0, trange0, river0, town0)

    stations.append(s0)

    s_id1 = "test-s-idB"
    m_id1 = "test-m-idB"
    label1 = "Station B"
    coord1 = (52.265989, 0.119921)
    trange1 = (-2.3, 3.4445)
    river1 = "River A"
    town1 = "Town B"
    s1 = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)

    stations.append(s1)

    s_id2 = "test-s-idC"
    m_id2 = "test-m-idC"
    label2 = "Station C"
    coord2 = (52.519327, 1.016386)
    trange2 = (-2.3, 3.4445)
    river2 = "River A"
    town2 = "Town C"
    s2 = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)

    stations.append(s2)

    s_id3 = "test-s-idD"
    m_id3 = "test-m-idD"
    label3 = "Station D"
    coord3 = (52.632525, 1.295940)
    trange3 = (-2.3, 3.4445)
    river3 = "River B"
    town3 = "Town D"
    s3 = MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)

    stations.append(s3)

    s_id4 = "test-s-idE"
    m_id4 = "test-m-idE"
    label4 = "Station E"
    coord4 = (52.454529, 5.525467)
    trange4 = (-2.3, 3.4445)
    river4 = "River B"
    town4 = "Town E"
    s4 = MonitoringStation(s_id4, m_id4, label4, coord4, trange4, river4, town4)

    stations.append(s4)

    Result = floodsystem.geo.stations_by_river(stations)
    assert Result == {'River A': ['Station A', 'Station B', 'Station C'], 'River B': ['Station D', 'Station E']}
test_stations_by_river()

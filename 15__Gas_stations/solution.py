def trip_not_posible(maximum_km, stations):
    check = any((stations[i + 1] - stations[i]) > maximum_km for i in range(len(stations) - 1))
    return check

def gas_stations(distance, tank_size, stations):
    stations_map = []
    stations = [station for station in stations if station < distance]
    stations.append(distance)
    maximum_km = tank_size

    if trip_not_posible(maximum_km, stations):
        return stations_map

    for i in range(len(stations)):
        if  stations[i] >= maximum_km:
            maximum_km = tank_size + stations[i - 1]
            stations_map.append(stations[i - 1])
            
    return stations_map

gas_stations(100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150])
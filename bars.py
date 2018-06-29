import json
import sys
import argparse
import math


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_biggest_bar(data):
    bars_seats_count = [bar['properties']['Attributes']['SeatsCount']
                        for bar in data['features']]
    index_of_bar = bars_seats_count.index(max(bars_seats_count, key=abs))
    return data['features'][index_of_bar]


def get_smallest_bar(data):
    bars_seats_count = [bar['properties']['Attributes']['SeatsCount']
                        for bar in data['features']]
    index_of_bar = bars_seats_count.index(min(bars_seats_count, key=abs))
    return data['features'][index_of_bar]


def get_distance(longitude1, latitude1, longitude2, latitude2):
    radian_longitude1 = longitude1 * math.pi / 180
    radian_latitude1 = latitude1 * math.pi / 180
    radian_longitude2 = longitude2 * math.pi / 180
    radian_latitude2 = latitude2 * math.pi / 180
    dlongitude = radian_longitude2 - radian_longitude1
    dlatitude = radian_latitude2 - radian_latitude1
    a = (math.sin(dlatitude / 2))**2 + math.cos(radian_latitude1) * \
        math.cos(radian_latitude2) * (math.sin(dlongitude / 2))**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    earth_radius = 6371
    distance = earth_radius * c
    return distance


def get_closest_bar(data, longitude, latitude):
    coordinates_of_bars = []
    for bar in data['features']:
        coordinates = bar['geometry']['coordinates']
        distance = get_distance(coordinates[0], coordinates[
            1], longitude, latitude)
        coordinates_of_bars.append(distance)
    index_of_bar = coordinates_of_bars.index(min(coordinates_of_bars))
    return data['features'][index_of_bar]


def print_result(data, filename):
    if filename:
        with open(filename, 'w+', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)
    else:
        print(data)


if __name__ == '__main__':
    i_filename = sys.argv[1]
    o_filename = ''
    if(len(sys.argv) == 3):
        o_filename = sys.argv[2]
    data = load_data(i_filename)

    print('Choose option:')
    print('1 - Find the biggest bar.')
    print('2 - Find the smallest one.')
    print('3 - Find the closest one.')
    option = int(input('Type option number: '))

    if option == 1:
        bar = get_biggest_bar(data)
        print_result(bar, o_filename)

    elif option == 2:
        bar = get_smallest_bar(data)
        print_result(bar, o_filename)

    elif option == 3:
        longitude = float(input('longitude: '))
        latitude = float(input('latitude: '))
        bar = get_closest_bar(data, longitude, latitude)
        print_result(bar, o_filename)

    else:
        raise ValueError('{0} is invalid option.'.format(option))

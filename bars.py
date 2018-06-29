import json
import sys
import argparse
import math


def load_data(filepath):
    with open(filepath, encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_biggest_bar(data):
    l = [el['properties']['Attributes']['SeatsCount']
         for el in data['features']]
    i = l.index(max(l, key=abs))
    return data['features'][i]


def get_smallest_bar(data):
    l = [el['properties']['Attributes']['SeatsCount']
         for el in data['features']]
    i = l.index(min(l, key=abs))
    return data['features'][i]


def get_distance(lon1, lat1, lon2, lat2):
    rad_lon1 = lon1 * math.pi / 180
    rad_lat1 = lat1 * math.pi / 180
    rad_lon2 = lon2 * math.pi / 180
    rad_lat2 = lat2 * math.pi / 180
    dlon = rad_lon2 - rad_lon1
    dlat = rad_lat2 - rad_lat1
    a = (math.sin(dlat / 2))**2 + math.cos(rad_lat1) * \
        math.cos(rad_lat2) * (math.sin(dlon / 2))**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R = 6371  # The radius of the Earth
    d = R * c
    return d


def get_closest_bar(data, longitude, latitude):
    l = []
    for el in data['features']:
        coordinates = el['geometry']['coordinates']
        qdistance = get_distance(coordinates[0], coordinates[
                                 1], longitude, latitude)
        l.append(qdistance)
    i = l.index(min(l))
    return data['features'][i]


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
        ret = get_biggest_bar(data)
        if len(o_filename) > 0:
            with open(o_filename, 'w+', encoding='utf-8') as f:
                json.dump(ret, f, ensure_ascii=False)
        else:
            print(ret)

    elif option == 2:
        ret = get_smallest_bar(data)
        if len(o_filename) > 0:
            with open(o_filename, 'w+', encoding='utf-8') as f:
                json.dump(ret, f, ensure_ascii=False)
        else:
            print(ret)

    elif option == 3:
        longitude = float(input('longitude: '))
        latitude = float(input('latitude: '))
        ret = get_closest_bar(data, longitude, latitude)
        if len(o_filename) > 0:
            with open(o_filename, 'w+', encoding='utf-8') as f:
                json.dump(ret, f, ensure_ascii=False)
        else:
            print(ret)

    else:
        raise ValueError('{0} is invalid option.'.format(option))

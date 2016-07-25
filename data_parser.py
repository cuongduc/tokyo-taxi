# Read the tokyo.txt
import os
import json
import copy
import numpy as np

NEW_TAXI_ROUTE = '=='
END_TAXI_FILE = '-->'

points = []


def read_taxi_info():
    input_file = 'data/taxi_info.txt'
    if not os.path.isfile(input_file):
        return False

    f = open(input_file, 'r')
    taxis = []

    lines = f.readlines()

    index = 0

    while (index < len(lines) / 3):
        line = lines[index]
        line = line.replace('\n', '')
        line = line.replace('\r', '')
        tokens = line.split(' ')
        if len(tokens) == 1:
            if not '-' in tokens[0]:
                next_line = lines[index + 1]
                toks = next_line.split(' ')
                first_post = toks[0]
                taxi = {
                    'id': int(tokens[0]),
                    'position': int(first_post)
                }
                taxis.append(taxi)
        index += 1
    s1 = [taxi['position'] for taxi in taxis]
    s2 = [point['id'] for point in points]
    common = set(s1) ^ set(s2)
    common = list(common)
    results = []
    for i in range(0, 100):
        index = np.random.randint(0, len(common))
        point_id = common[index]

        item = {
            'id': point_id,
            'lat': points[point_id]['lat'],
            'lng': points[point_id]['lng']
        }
        results.append(item)
    return results


# Xu ly data, ve ban do
def read_data():
    input_file = 'data/reduceGraph2.txt'
    if not os.path.isfile(input_file):
        return False

    file = open(input_file, 'r')

    # points = []
    vertices = []
    switch = False

    for line in file:
        line = line.replace('\n', '')
        line = line.replace('\r', '')
        tokens = line.split(' ')
        flag = int(tokens[0])

        if flag == -1:  # end reading long lat
            switch = True
            continue

        if switch:
            item = {
                'start'     : int(tokens[0]),
                'end'       : int(tokens[1]),
                'distance'  : float(tokens[2]),
                'type'      : int(tokens[3])
            }
            vertices.append(item)
        else:
            item = {
                'id': int(tokens[0]),
                'lng': float(tokens[1]),
                'lat': float(tokens[2])
            }
            points.append(item)
    return points, vertices

# Xu ky request


def read_request_data(sid, all=None):
    input_file = 'data/outputByTime_05_09_08_43_58.txt'

    if not os.path.isfile(input_file):
        return False

    f = open(input_file, 'r')

    requests = []
    request = {}
    flow = 'forward'
    new_request = False

    points, _ = read_data()

    for line in f:
        # Replace end-line characters
        line = line.replace('\n', '')
        line = line.replace('\r', '')
        tokens = line.split(' ')

        if tokens[0] == NEW_TAXI_ROUTE:
            continue

        if tokens[0] == END_TAXI_FILE:
            requests.append(request)
            break

        if 'R+' in tokens[0]:
            if request:
                requests.append(request)
            flow = 'forward'
            rid = int(tokens[1])

            if tokens[2] == 'true':
                request = {
                    'id': rid,
                    'forward': [],
                    'backward': [],
                    'type': 'people'
                }
            else:
                request = {
                    'id': rid,
                    'forward': [],
                    'backward': [],
                    'type': 'parcel'
                }
        else:
            if 'R-' in tokens[0]:
                flow = 'backward'
                continue
            vertex = int(tokens[0])
            time = float(tokens[1])
            request[flow].append({
                'vertex': vertex,
                'time': time,
                'lat': points[vertex]['lat'],
                'lng': points[vertex]['lng'],
            })

    f.close()

    if all is False:
        for re in requests:
            if re['id'] == sid:
                return re
    return request

def read_all_request_data():
    input_file = 'data/outputByTime_05_09_08_43_58.txt'

    if not os.path.isfile(input_file):
        return False

    f = open(input_file, 'r')

    requests = []
    request = {}
    flow = 'forward'
    new_request = False

    points, _ = read_data()
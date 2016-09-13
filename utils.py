import urllib2
from sqlalchemy import text

SERVICE_PATH = 'http://108.61.200.110:8080/SRAP/webresources/welcome?' \
    'requeststring=1+0+9439+12492+1800+2400+1800+6002+857489.46+857489.46'


def request_route_from_webservice():
    response = urllib2.urlopen(SERVICE_PATH)
    result = response.read()

    result_set = result.split('\n')
    result_set.pop()  # remove last element as it's empty

    is_forwarding = True
    is_carrying_passenger = False
    forward_path = {
        "is_carrying_passenger": False,
        "points": []
    }
    backward_path = {
        "is_carrying_passenger": False,
        "points": []
    }

    for line in result_set:
        item = line.split(' ')
        if 'R+' in line:
            is_forwarding = True
            if 'true' in item:
                is_carrying_passenger = True
            else:
                is_carrying_passenger = False
            forward_path["is_carrying_passenger"] = is_carrying_passenger
        elif 'R-' in line:
            is_forwarding = False
            if 'true' in item:
                is_carrying_passenger = True
            else:
                is_carrying_passenger = False
            backward_path["is_carrying_passenger"] = is_carrying_passenger
        else:
            if is_forwarding:
                forward_path["points"].append(item[0])
            else:
                backward_path["points"].append(item[0])

    return forward_path, backward_path


def serialize_points_list(db, path):
    length = len(path['points'])
    for i in range(0, length):
        point = int(path['points'][i])
        converted_point = match_point_to_real_coordinates(db, point)
        path['points'][i] = converted_point[0].encode('utf-8')

    print(path)
    return path


def match_point_to_real_coordinates(db, point_id):
    sql = text(
        'SELECT ST_AsGeoJson(geometry) FROM points WHERE id = {}'
        .format(point_id)
    )
    result = db.engine.execute(sql)
    points = []
    for row in result:
        points.append(row[0])
    return points

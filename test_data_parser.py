from data_parser import read_data, read_request_data
import json

# points, vertices = read_data()

dump = read_request_data(10)
print(dump)

# synthesized_vertices = []

# for vertex in vertices:
# 	item = {
# 		'type': vertex['type'],
# 		'start' : {
# 			'lat' : points[vertex['start']]['lat'],
# 			'lng' : points[vertex['start']]['lng']
# 		},
# 		'end' : {
# 			'lat' : points[vertex['end']]['lat'],
# 			'lng' : points[vertex['end']]['lng']
# 		}
# 	}

# 	synthesized_vertices.append(item)

# print(json.dumps(synthesized_vertices))
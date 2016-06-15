from data_parser import read_data, read_request_data, read_taxi_info
import json
import time
# points, vertices = read_data()
read_data()
start = time.time()
common = read_taxi_info()
done = time.time()
elapsed = done - start
print(common)
print(elapsed)

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
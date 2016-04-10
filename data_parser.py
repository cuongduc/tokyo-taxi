# Read the tokyo.txt
import os
import json
import copy

NEW_TAXI_ROUTE = '=='
END_TAXI_FILE = '-->'

def read_data():
	input_file = 'data/reduceGraph2.txt'
	if not os.path.isfile(input_file):
		return False

	file = open(input_file, 'r')

	points = []
	vertices = []
	switch = False

	for line in file:
		line = line.replace('\n','')
		line = line.replace('\r','')
		tokens = line.split(' ')
		flag = int(tokens[0])

		if flag == -1: # end reading long lat
			switch = True
			continue

		if switch:
			item = {
				'start' 	: int(tokens[0]),
				'end'		: int(tokens[1]),
				'distance'	: float(tokens[2]),
				'type'		: int(tokens[3])
			}
			vertices.append(item)
		else:
			item = {
				'id' : int(tokens[0]),
				'lng': float(tokens[1]),
				'lat': float(tokens[2])
			}
			points.append(item)
	return points, vertices

def read_request_data(sid):
	input_file = 'data/output_test.txt'

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
			request = {
				'id' : rid,
				'forward' : [],
				'backward' : []
				}
		else:
			if 'R-' in tokens[0]:
				flow = 'backward'
				continue
			vertex = int(tokens[0])
			request[flow].append({
				'vertex' : vertex,
				'lat'	 : points[vertex]['lat'],
				'lng'	 : points[vertex]['lng'],
			})

	f.close()

	for re in requests:
		if re['id'] == sid:
			return re


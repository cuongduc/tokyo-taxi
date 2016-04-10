# Read the tokyo.txt
import os
import json

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
				'type'		: int(tokens[3]),
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
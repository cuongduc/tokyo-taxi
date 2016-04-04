# Read the tokyo.txt
import os
import json

def read_data():
	input_file = 'data/tokyo.txt'
	
	if not os.path.isfile(input_file):
		return False

	file = open(input_file, 'r')
	
	points = []

	for line in file:
		line = line.replace('\n','')
		tokens = line.split(',')
		flag = int(tokens[0])

		if flag == -1:
			break
		else:
			item = {
				# 'id' : tokens[0],
				'lng': float(tokens[1]),
				'lat': float(tokens[2])
			}

			points.append(item)

	return points

def read_
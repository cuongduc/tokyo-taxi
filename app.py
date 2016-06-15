from flask import Flask, render_template, jsonify, request
from data_parser import read_data, read_request_data, read_taxi_info
import copy

app = Flask(__name__)

# Define some terminated constant
NEW_TAXI_ROUTE = '=='
END_TAXI_FILE = '-->'


@app.route('/')
def main():
	return render_template("home.html")
	# return render_template("index.html")

@app.route('/passenger')
def passenger():
	return render_template("index.html")
# @app.route('/home')
# def home():
# 	return render_template("home.html")


@app.route('/getMapData', methods=['POST'])
def get_map_data():
	# read the tokyo.txt file
	points, vertices = read_data()

	synthesized_vertices = []

	for vertex in vertices:
		item = {
			'type': vertex['type'],
			'start' : {
				'lat' : points[vertex['start']]['lat'],
				'lng' : points[vertex['start']]['lng']
			},
			'end' : {
				'lat' : points[vertex['end']]['lat'],
				'lng' : points[vertex['end']]['lng']
			}
		}
		synthesized_vertices.append(item)
		
	return jsonify(data=synthesized_vertices)

@app.route('/getTaxisList', methods=['POST'])
def get_taxi_info():
	taxis = read_taxi_info()

	return jsonify(data=taxis)

@app.route('/directions', methods=['POST'])
def get_directions_for_request():
	rid = request.form['request']
	rid = int(rid)
	r = read_request_data(rid)
	return jsonify(data=r)

if __name__ == '__main__':
	app.debug = True
	app.run()
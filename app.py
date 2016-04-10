from flask import Flask, render_template, jsonify, request

from data_parser import read_data

app = Flask(__name__)

@app.route('/')
def main():
	return render_template("index.html")

@app.route('/getMapData', methods=['POST'])
def getMapData():
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

if __name__ == '__main__':
	app.run()
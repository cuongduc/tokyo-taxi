from flask import Flask, render_template, jsonify, request

from data_parser import read_data

app = Flask(__name__)

@app.route('/')
def main():
	return render_template("index.html")

@app.route('/getMapData', methods=['POST'])
def getMapData():
	# read the tokyo.txt file
	raw_string = read_data()
	return jsonify(data=raw_string)

if __name__ == '__main__':
	app.run()
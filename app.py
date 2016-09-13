from flask import Flask, render_template, jsonify, request, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from data_parser import read_data, read_request_data, read_taxi_info
from forms import ParcelRequestForm
from data.parcel_request import *
from utils import *
import sys
# import random

reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/tokyo_taxi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define some terminated constant
NEW_TAXI_ROUTE = '=='
END_TAXI_FILE = '-->'


@app.route('/', methods=['GET', 'POST'])
def main():
    form = ParcelRequestForm(request.form)
    if request.method == 'POST':
        global parcel_request
        parcel_request = {
            'parcel_type': form.parcel_type.data,
            'parcel_weight': form.parcel_weight.data,
            'parcel_dimension': form.parcel_dimension.data,
            'parcel_arrive_time': form.parcel_arrive_time.data,
            'parcel_fee': form.parcel_fee.data,
            'parcel_note': form.parcel_note.data,
            'parcel_place': form.parcel_place.data
        }
        persist_parcel_request_data(parcel_request)
        return redirect('/passenger')
    return render_template("home.html", form=form)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')


@app.route('/passenger')
def passenger():
    parcel = {
        'parcel_type': PARCEL_TYPE,
        'parcel_weight': PARCEL_WEIGHT,
        'parcel_dimension': PARCEL_DIMENSION,
        'parcel_arrive_time': PARCEL_ARRIVE_TIME,
        'parcel_fee': PARCEL_FEE,
        'parcel_note': PARCEL_NOTE,
        'parcel_place': PARCEL_PLACE
    }

    return render_template("index.html", parcel=parcel)


@app.route('/getMapData', methods=['POST'])
def get_map_data():
    # read the tokyo.txt file
    points, vertices = read_data()

    synthesized_vertices = []

    for vertex in vertices:
        item = {
            'type': vertex['type'],
            'start': {
                'lat': points[vertex['start']]['lat'],
                'lng': points[vertex['start']]['lng']
            },
            'end': {
                'lat': points[vertex['end']]['lat'],
                'lng': points[vertex['end']]['lng']
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
    # Get routes from remote webservice
    forward_path, backward_path = request_route_from_webservice()
    forward_path = serialize_points_list(db, forward_path)
    backward_path = serialize_points_list(db, backward_path)

    return jsonify(data=[forward_path, backward_path])
# def get_directions_for_request():
#     # request_list = [16805, 8909, 12958, 3579, 250]
#     request_list = [250]
#     rid = random.choice(request_list)
#     # rid = request.form['request']
#     # rid = int(rid)
#     r = read_request_data(rid)
#     return jsonify(data=r)


@app.route('/all_directions', methods=['POST'])
def get_all_directions_for_requests():
    request_list = [16805, 8909, 12958, 3579, 250]
    r = read_request_data(request_list, all=True)
    return jsonify(data=r)


def persist_parcel_request_data(parcel):
    f = open('data/parcel_request.py', 'w')
    f.writelines('# -*- encoding: utf-8 -*-\n')
    f.writelines("PARCEL_TYPE='" + str(parcel['parcel_type']) + "'\n")
    f.writelines("PARCEL_WEIGHT='" + str(parcel['parcel_weight']) + "'\n")
    f.writelines("PARCEL_DIMENSION='" +
                 str(parcel['parcel_dimension']) + "'\n")
    f.writelines("PARCEL_ARRIVE_TIME='" +
                 str(parcel['parcel_arrive_time']) + "'\n")
    f.writelines("PARCEL_FEE='" + str(parcel['parcel_fee']) + "'\n")
    f.writelines("PARCEL_NOTE='" + str(parcel['parcel_note']) + "'\n")
    f.writelines("PARCEL_PLACE='" + str(parcel['parcel_place']) + "'\n")

    f.close()


@app.route('/test', methods=['GET'])
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.debug = True
    app.run()

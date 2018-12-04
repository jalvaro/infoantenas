from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def healthcheck():
    return jsonify(status='healthy!')

def get_rectangle(request):
    return {
        'point1': {
            'lat': request.args['lat1'],
            'lng': request.args['lng1']
        },
        'point2': {
            'lat': request.args['lat2'],
            'lng': request.args['lng2']
        }
    }

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_point_malformed(point):
    return point is None or point['lat'] is None or point['lng'] is None or not is_number(point['lat']) or not is_number(point['lng'])

@app.route('/antennas')
def get_anthens_info():
    rectangle = get_rectangle(request)

    if rectangle is None or is_point_malformed(rectangle['point1']) or is_point_malformed(rectangle['point2']):
        return jsonify({})

    point1 = rectangle['point1']
    point2 = rectangle['point2']

    bbox = ','.join([point1['lng'], point1['lat'], point2['lng'], point2['lat']])
    payload = {
        'idCapa': 'null',
#        'bbox': '-3.3525553686015,41.838103675076,-3.3428779584757,41.844144009778',
        'bbox': bbox,
        'zoom': 4
    }
    r = requests.get('https://geoportal.minetur.gob.es/VCTEL/infoantenasGeoJSON.do', params=payload)
    print(r.json())
    return jsonify(r.json())

def get_app():
    return app

if __name__ == '__main__':
    app.run(port=5000)

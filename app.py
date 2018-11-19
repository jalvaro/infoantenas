from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def healthcheck():
    return jsonify(status='healthy!')

@app.route('/antennas')
def get_anthens_info():
    r = requests.get('https://geoportal.minetur.gob.es/VCTEL/infoantenasGeoJSON.do?idCapa=null&bbox=-3.3525553686015%2C41.838103675076%2C-3.3428779584757%2C41.844144009778&zoom=4')
    return jsonify(r.json())

def get_app():
    return app

if __name__ == '__main__':
    app.run(port=5000)

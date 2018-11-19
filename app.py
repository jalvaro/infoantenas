from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def healthcheck():
    return jsonify(status='healthy!')

def get_app():
    return app

if __name__ == '__main__':
    app.run(port=5000)

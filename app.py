from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def healthcheck():
        return jsonify(status='healthy!')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)

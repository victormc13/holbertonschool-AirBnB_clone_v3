#!/usr/bin/python3

"""Connect to API using Flask"""

import os
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_storage(exception):
    """Close the storage"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 error and return JSON response"""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True)

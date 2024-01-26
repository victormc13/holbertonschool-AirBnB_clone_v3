#!/usr/bin/python3

"""Index"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """Get API status"""
    return jsonify({"status": "OK"})
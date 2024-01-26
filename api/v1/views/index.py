#!/usr/bin/python3

"""Index"""

from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """Get API status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=True)
def number_objects():
    """Retrieves the number of each objects by type"""
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    num_objs = {name: storage.count(obj) for obj, name in zip(classes, names)}
    return jsonify(num_objs)

#!/usr/bin/python3

"""City objects that handles all default RESTFul API actions"""

from models.city import City
from models.state import State
from models import storage
from api.v1.views import app_views
from flask import jsonify, request, make_response, abort


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities(state_id):
    """Get list of all City objects by a specific State"""
    state = storage.get(State, state_id)
    if state:
        list_cities = [city.to_dict() for city in state.cities]
        return jsonify(list_cities)
    else:
        abort(404)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """Get a City object by id"""
    city = storage.get(City, city_id)
    if city:
        return jsonify(city.to_dict())
    else:
        abort(404)


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_city(city_id):
    """Delete a City object by id"""
    city = storage.get(City, city_id)
    if city:
        storage.delete(city)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_city(state_id):
    """Create a new City"""
    state = storage.get(State, state_id)
    data = request.get_json()
    if not state:
        abort(404)
    if not data:
        abort(400, description="Not a JSON")
    if 'name' not in data:
        abort(400, description="Missing name")

    new_city = City(**data)
    new_city.state_id = state.id
    new_city.save()
    return make_response(jsonify(new_city.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def put_city(city_id):
    """Update a City object by id"""
    city = storage.get(City, city_id)
    if city:
        data = request.get_json()
        if not data:
            abort(400, description="Not a JSON")

        for key, value in data.items():
            if key not in ["id", "state_id", "created_at", "updated_at"]:
                setattr(city, key, value)

        storage.save()
        return make_response(jsonify(city.to_dict()), 200)
    else:
        abort(404)

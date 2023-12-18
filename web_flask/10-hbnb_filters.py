#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from operator import attrgetter


app = Flask(__name__)


def sort_by_name(obj):
    return obj.name


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """/states_list route"""
    states = storage.all(State)
    states_sorted = sorted(states, key=sort_by_name)

    cities = []
    for state in states_sorted:
        cities.extend(sorted(state.cities, key=sort_by_name))

    amenities = storage.all(Amenity).values()
    amenities_sorted = sorted(amenities, key=sort_by_name)

    return render_template('10-hbnb_filters.html', states=states_sorted,
                           cities=cities,
                           amenities=amenities_sorted)


@app.teardown_appcontext
def session_close(exception):
    """Close the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

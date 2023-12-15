#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from operator import attrgetter

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def sorted_state():
    """List of all State objects present in DBStorage"""
    states = storage.all(State).values()
    states_sorted = sorted(states, key=attrgetter('name'))
    return render_template('7-states_list.html', states=states_sorted)

@app.route('/cities_by_states', strict_slashes=False)
def sorted_cities_states():
    """List of all Cities objects present in State"""
    states = storage.all(State).values()
    cities_sorted = []
    for state in states:
        cities = sorted(state.cities, key=attrgetter('name'))
        cities_sorted.extend(cities)
    return render_template('8-cities_by_states.html', cities=cities_sorted)

@app.teardown_appcontext
def session_close(exception):
    """Close the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

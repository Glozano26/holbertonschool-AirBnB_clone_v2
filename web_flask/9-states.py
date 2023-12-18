#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from operator import attrgetter


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """/states_list route"""
    states_list = list(storage.all(State).values())
    states_list.sort(key=lambda x: x.name)
    return render_template('9-states.html', states=states_list)


@app.route('/states/<id>', strict_slashes=False)
def state_cities_list(id=None):
    """Displays cities of a specific State"""
    e = None
    states = storage.all(State)
    c = list(storage.all(City).values())
    c.sort(key=lambda x: x.name)
    if id:
        key = "State." + id
        if key in states.keys():
            e = states[key]
    return render_template('9-states.html', cities=c, state=e, id=id)


@app.teardown_appcontext
def session_close(exception):
    """Close the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from operator import attrgetter


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def sorted_state():
    """list of all State objects present in DBStorage"""
    states = storage.all(State).values()
    states_sorted = sorted(states, key=attrgetter('name'))
    return render_template('7-states_list.html', states=states_sorted)


@app.teardown_appcontext
def session_close(exception):
    """close the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

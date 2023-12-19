from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def display_filters():
    states = storage.all(State)
    amenities = storage.all(Amenity)
    cities = storage.all(City)
    return render_template('10-hbnb_filters.html', states=states,
                           city= cities,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
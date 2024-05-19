#!/usr/bin/python3
"""starts web application listening on 0.0.0.0, port 5000"""
from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays cities by their states with city id and name"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

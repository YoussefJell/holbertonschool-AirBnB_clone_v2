#!/usr/bin/env python3
"""6-number_odd_or_even Module"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_sqlalchemy_sess(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def cities_by_states():
    """Displays html page"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', my_dict=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0")

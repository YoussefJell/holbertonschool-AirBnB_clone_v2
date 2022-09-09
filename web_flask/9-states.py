#!/usr/bin/python3
"""9-states Module"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_sqlalchemy_sess(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states/', strict_slashes=False)
def list_states():
    """Displays html page"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', my_dict=states)


@app.route('/states/<id>', strict_slashes=False)
def many_states(id):
    """Displays html page"""
    states = storage.all(State).values()
    my_cities = list()

    for state in states:
        if id and state.id == id:
            for city in state.cities:
                if city.state_id == state.id:
                    my_cities.append(city)
        elif not id:
            for city in state.cities:
                if city.state_id == state.id:
                    my_cities.append(city)
    return render_template('8-cities_by_states.html',
                           my_state=states, my_cities=my_cities)


if __name__ == '__main__':
    app.run(host="0.0.0.0")

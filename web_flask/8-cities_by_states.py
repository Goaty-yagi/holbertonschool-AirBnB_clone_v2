#!/usr/bin/python3

from flask import Flask, render_template

from models.__init__ import storage, DBStorage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return f'C {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', number=n)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)

@app.teardown_appcontext
def teardown_app_context(exception=None):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)

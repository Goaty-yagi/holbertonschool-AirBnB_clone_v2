#!/usr/bin/python3
"""
This module provides flask app routing certain view pages.
"""
from flask import Flask, render_template

from models.__init__ import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)

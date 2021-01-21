#!/usr/bin/python3
""" List of states """


from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """display states"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """display states"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
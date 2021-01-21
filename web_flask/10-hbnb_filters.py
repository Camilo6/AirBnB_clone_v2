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


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """Dcities by states"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)

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


@app.route("/states_list", strict_slashes=False)
def states_list():
    """display states"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.route("/hbnb_filters", strict_slashes=False)
def display_filters():
    state_obj = storage.all("State")
    city_obj = storage.all("City")
    amenities_objs = storage.all("Amenity")
    states = list()
    cities = list()
    amenities = list()
    for state, value in state_obj.items():
        states.append(value)
    for city, value in city_obj.items():
        cities.append(value)
    for amenity, value in amenities_objs.items():
        amenities.append(value)

    return render_template("10-hbnb_filters.html",
                           states=states,
                           cities=cities,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

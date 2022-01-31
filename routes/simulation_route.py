from flask import Blueprint, jsonify

# TODO: define the ref to its react front-end
# TODO: GET and POST logic

# create instance of bluprint and set name
simulation = Blueprint("simulation", __name__)

# mapping method/function to http request
@simulation.route("/", methods =['GET', 'POST'])
def simulation_route():
    return jsonify({"SHOW": "SIMULATION-WINDOW"})

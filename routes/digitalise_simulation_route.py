from flask import Blueprint, jsonify

# TODO: define the ref to its react front-end
# TODO: GET and POST logic

# create instance of bluprint and set name
digitalise = Blueprint("digitalise", __name__)

# mapping method/function to http request
@digitalise.route("/", methods =['GET', 'POST'])
def digitalise_route():
    return jsonify({"SHOW": "digitalise-SIMULATION-WINDOW"})

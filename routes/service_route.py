from flask import Blueprint, jsonify

# TODO: define the ref to its react front-end
# TODO: GET and PUT logic

# create instance of bluprint and set name
service = Blueprint("service", __name__)

# mapping method/function to http request
@service.route("/", methods =['GET', 'PUT'])
def service_route():
    return jsonify({"Get List": "service"})

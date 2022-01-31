from flask import Blueprint, jsonify

# TODO: define the ref to uts react front-end
# TODO: GET and PUT logic

# create instance of bluprint and set name
department = Blueprint("department", __name__)

# mapping method/function to http request
@department.route("/", methods =['GET', 'PUT'])
def department_route():
    return jsonify({"Get List": "departments"})

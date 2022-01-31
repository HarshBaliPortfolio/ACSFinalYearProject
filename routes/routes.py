from flask import Blueprint, jsonify

# TODO: define the ref to static or template folder 

# create instance of bluprint and set name
welcome = Blueprint("welcome", __name__)

# mapping method/function to http request
@welcome.route("/", methods =['GET'])
def hello_world():
    return jsonify({"hello":"flask!"})

#from main import app
from flask import Flask , jsonify, request

from flask_cors import CORS



# TODO warmup period in **simulation module**
    # TODO record the **input/output data** in csv file
#TODO: in future might need bussiness logic for data visualisation
    #TODO: update routes for visualisation



# Tell python we r creating flask web app
app = Flask(__name__)
CORS(app)

#marshmallow obj for serialisation


app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:Bali!997@localhost/simulation_data'

#TODO: get, update, post, del for other methods
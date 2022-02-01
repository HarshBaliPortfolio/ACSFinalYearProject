import imp
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
# Tell python we r creating flask web app
app = Flask(__name__)

#marshmallow obj for serialisation
ma = Marshmallow(app)

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:Bali!997@localhost/simulation_data'

#TODO: get, update, post, del for other methods

db = SQLAlchemy(app)

from .department import department
app.register_blueprint(department, url_prefix='/departments')

#registers blueprint or informs the route
#app.register_blueprint(department, url_prefix="/departments")

#app.register_blueprint(simulation, url_prefix="/departments/services/simulation")
#app.register_blueprint(digitalise , url_prefix="/departments/services/simulation/digitalise")

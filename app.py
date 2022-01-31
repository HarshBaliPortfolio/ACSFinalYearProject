import email
from sys import prefix
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
#routes is in different package
from routes.department_route import department
from routes.service_route import service
from routes.simulation_route import simulation
from routes.digitalise_simulation_route import digitalise




# Tell python we r creating flask web app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:Bali!997@localhost/simulation_data'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False'

# TODO: probably put the blueprints under departments
#registers blueprint or informs the route
app.register_blueprint(department, url_prefix="/departments")
app.register_blueprint(service, url_prefix="/departments/services")
app.register_blueprint(simulation, url_prefix="/departments/services/simulation")
app.register_blueprint(digitalise , url_prefix="/departments/services/simulation/digitalise")

# instanciate sqlalchemy
db = SQLAlchemy(app)

# creates a table for the schema
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __init__(self, username):
      self.username=username
      self.email=email




# run the app in dev mode
if __name__ == "__main__":
    app.run(debug=True)
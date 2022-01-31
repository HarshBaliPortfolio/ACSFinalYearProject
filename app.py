from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false
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

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique= True, nullable = False)
    department_name = db.Column(db.String(200),nullable = False )
    #back ref for services
    services = db.relationship('Service', backref='department')


class Service(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique= True, nullable = False)
  service_name = db.Column(db.String(200),  nullable = False)
  #defining foreign key
  department_id= db.Column(db.Integer, db.ForeignKey('department.id'))
  #back ref for qsimulations
  qsimulations = db.relationship('QSimulation', backref='service')



class Simulation(db.Model):
  id = db.Column(db.Integer, primary_key=True, nullable = False)
  warm_up_duration = db.Column(db.Float, nullable = False)
  total_duration = db.Column(db.Float,  nullable = False )
  patient_interval_time = db.Column(db.Float, nullable = False)
  approx_triage_time= db.Column(db.Float, nullable = False)
  approx_booking_time= db.Column(db.Float, nullable = False)
  receptionist_no = db.Column(db.Integer, nullable = False)
  triage_nurse_no = db.Column(db.Integer, nullable = False)
  booking_iot_no = db.Column(db.Integer, nullable = True)
  triage_iot_no = db.Column(db.Integer, nullable = True)
  #defining foreign key
  service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
  #back ref for qsimulationruns
  qsimulation_runs = db.relationship('SimulationRun', backref='qsimulation')



class SimulationRun(db.Model):
   id = db.Column(db.Integer, primary_key=True,  nullable = False)
   run_no = db.Column(db.Integer, nullable = False)
   patient_no = db.Column(db.Integer, nullable = False)
   time_spent_in_booking_q = db.Column(db.Float)
   time_spent_while_booking = db.Column(db.Float)
   time_spent_in_triage_q= db.Column(db.Float)
   time_spent_while_triaging = db.Column(db.Float)
   total_time_spent = db.Column(db.Float)
   #defining foreign key
   qsimulation_id= db.Column(db.Integer, db.ForeignKey('simulation.id'))
    
#from app import db
#db.create_all()


# run the app in dev mode
if __name__ == "__main__":
    app.run(debug=True)
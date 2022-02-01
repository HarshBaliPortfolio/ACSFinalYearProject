from dataclasses import fields
from email.policy import default
from flask import Flask, jsonify, url_for, request
from flask_sqlalchemy import SQLAlchemy
#routes is in different package
#from routes.department_route import department
#from routes.service_route import service
#from routes.simulation_route import simulation
#from routes.digitalise_simulation_route import digitalise
from flask_marshmallow import Marshmallow
import datetime




# Tell python we r creating flask web app
app = Flask(__name__)

#marshmallow obj for serialisation
ma = Marshmallow(app)

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:Bali!997@localhost/simulation_data'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False'

# TODO: FIGURE OUT THE WAY TO USE BLUE PRINTS AND MODELS IN SEP MODULE
#registers blueprint or informs the route
#app.register_blueprint(department, url_prefix="/departments")
#app.register_blueprint(service, url_prefix="/departments/services")
#app.register_blueprint(simulation, url_prefix="/departments/services/simulation")
#app.register_blueprint(digitalise , url_prefix="/departments/services/simulation/digitalise")

# instanciate sqlalchemy

#TODO: get, update, post, del for other methods

db = SQLAlchemy(app)

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique= True, nullable = False)
    department_name = db.Column(db.String(200),nullable = False )
    #back ref for services
    services = db.relationship('Service', backref='department')

    #required to create a department to hold the json input
    def __init__(self, department_name):
      self.department_name =department_name


class DepartmentSchema(ma.Schema):
  class Meta:
    fields = ("id", "department_name")

department_schema = DepartmentSchema()
#serialise query set
# need to fetch list of departments
departments_schema = DepartmentSchema(many= True)


#add department
@app.route('/departments', methods =['POST'])
def add_department():
    #fetching the input from user
    department_name = request.json['department_name']
    #creating a model and passing the input
    department = Department(department_name)
    # adding to db
    db.session.add(department)
    db.session.commit()
    # returning jsonify of 1 department
    return department_schema.jsonify(department)

# get list of departments
@app.route('/departments', methods =['GET'])
def list_departments():
  #fetch all departments from mysql
  all_department = Department.query.all()
  # dump the results into department schema and serilise/deserialise it
  list_departments = departments_schema.dump(all_department)
  return jsonify(list_departments)

# get department by id 
@app.route('/departments/<id>/', methods =['GET'])
def get_department(id):
    #Query db
  department = Department.query.get(id)
    #return the jsonify in schema
  return department_schema.jsonify(department)

#update
@app.route('/departments/update/<id>/', methods =['PUT'])
def update_department(id):
  department = Department.query.get(id)
  #get the new value
  department_name = request.json['department_name']
  #the previous value = new value
  department.department_name = department_name
  #commit the change
  db.session.commit()
  #return the update 
  return department_schema.jsonify(department)

@app.route('/departments/delete/<id>/', methods =['DELETE'])
def delete_department(id):
  #GET DEP
  department = Department.query.get(id)
  #del it and commit
  db.session.delete(department)
  db.session.commit()
  # get all dep 
  all_department = Department.query.all()
  #dump all dep in dep schema
  list_departments = departments_schema.dump(all_department)
  #jsonify it
  return jsonify(list_departments)


class Service(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique= True, nullable = False)
  service_name = db.Column(db.String(200),  nullable = False)
  #defining foreign key
  department_id= db.Column(db.Integer, db.ForeignKey('department.id'))
  #back ref for qsimulations
  qsimulations = db.relationship('Simulation', backref='service')

  def __init__(self, service_name):
      self.department_name =service_name




class Simulation(db.Model):
  id = db.Column(db.Integer, primary_key=True, nullable = False)
  simulation_name = db.Column(db.String(200),  nullable = False)
  date = db.Column(db.DateTime, default=datetime.datetime.now)

  #Foreign key
  service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
  #backref for Q_Simulation
  q_simulation = db.relationship('QueSimulation', backref='simulation')

class QueSimulation(db.Model):
  #Columns
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

  #Foreign key
  simulation_id = db.Column(db.Integer, db.ForeignKey('simulation.id'))
  #backref for QSimulationrun
  q_simulation_run= db.relationship('QSimulationRun', backref='que_simulation.id')





class QueSimulationRun(db.Model):
   id = db.Column(db.Integer, primary_key=True,  nullable = False)
   run_no = db.Column(db.Integer, nullable = False)
   patient_no = db.Column(db.Integer, nullable = False)
   time_spent_in_booking_q = db.Column(db.Float)
   time_spent_while_booking = db.Column(db.Float)
   time_spent_in_triage_q= db.Column(db.Float)
   time_spent_while_triaging = db.Column(db.Float)
   total_time_spent = db.Column(db.Float)
   #defining foreign key
   qsimulation_id= db.Column(db.Integer, db.ForeignKey('que_simulation.id'))
    
#from app import db
#db.create_all()






# run the app in dev mode
if __name__ == "__main__":
    app.run(debug=True)
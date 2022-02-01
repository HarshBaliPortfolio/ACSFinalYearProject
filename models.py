from main import db, ma 
import datetime



#DEPARTMENT
#MODEL FOR DB
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique= True, nullable = False)
    department_name = db.Column(db.String(200),nullable = False )
    #back ref for services
    services = db.relationship('Service', backref='department')

    #required to create a department to hold the json input
    def __init__(self, department_name):
      self.department_name =department_name

#Schema for serialisation and desirialisation
class DepartmentSchema(ma.Schema):
  class Meta:
    fields = ("id", "department_name")

#Schema objects for routes
department_schema = DepartmentSchema()
departments_schema = DepartmentSchema(many= True)


#Service MODEL
class Service(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique= True, nullable = False)
  service_name = db.Column(db.String(200),  nullable = False)
  #defining foreign key
  department_id= db.Column(db.Integer, db.ForeignKey('department.id'), nullable =False)
  #back ref for qsimulations
  qsimulations = db.relationship('Simulation', backref='service')

  def __init__(self, service_name, department_id):
    self.service_name = service_name
    self.department_id = department_id


#Schema for serialisation and desirialisation
class ServiceSchema(ma.Schema):
  class Meta:
    fields = ("id", "service_name", "department_id")

#Schema objects for routes
service_schema = ServiceSchema()
services_schema = ServiceSchema(many= True)




#SIMULATION MODEL
class Simulation(db.Model):
  id = db.Column(db.Integer, primary_key=True, nullable = False)
  simulation_name = db.Column(db.String(200),  nullable = False)
  date = db.Column(db.DateTime, default=datetime.datetime.now)
  #Foreign key
  service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
  #backref for Q_Simulation
  q_simulation = db.relationship('QueSimulation', backref='simulation')
  
  def __init__(self,simulation_name):
    self.simulation_name= simulation_name

#Schema for serialisation and desirialisation
class SimulationSchema(ma.Schema):
  class Meta:
    fields = ("id", "simulation_name", "date", "service_id")

#Schema objects for routes
simulation_schema= SimulationSchema()
simulations_schema = SimulationSchema(many= True)




#QUESIMULATION MODEL
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
  q_simulation_run= db.relationship('QueSimulationRun', backref='que_simulation.id')

  def __init__(self, warm_up_duration,total_duration,
  patient_interval_time,approx_triage_time,approx_booking_time,
   receptionist_no, triage_nurse_no,  booking_iot_no, triage_iot_no):

   self.warm_up_duration= warm_up_duration
   self.total_duration =total_duration
   self.patient_interval_time =patient_interval_time
   self.approx_triage_time= approx_triage_time
   self.approx_booking_time =approx_booking_time
   self.receptionist_no =receptionist_no
   self.triage_nurse_no =triage_nurse_no
   self.booking_iot_no=booking_iot_no
   self.triage_iot_no=triage_iot_no

#Schema for serialisation and desirialisation
class QueSimulationSchema(ma.Schema):
  class Meta:
    fields = ("id", "warm_up_duration", "total_duration", "patient_interval_time", 
    "approx_triage_time", "approx_booking_time","receptionist_no","triage_nurse_no",
    "booking_iot_no", "triage_iot_no", "simulation_id")

#Schema objects for routes
que_simulation_schema= QueSimulationSchema()
que_simulations_schema = QueSimulationSchema(many= True)
   





#QueSimulationRun MODEL
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
   
   def __init__(self,run_no,patient_no,time_spent_in_booking_q,  
   time_spent_while_booking,time_spent_in_triage_q, 
   time_spent_while_triaging,total_time_spent  ):
    self.run_no =run_no
    self.patient_no=patient_no
    self.time_spent_in_booking_q =time_spent_in_booking_q
    self.time_spent_while_booking=time_spent_while_booking
    self.time_spent_in_triage_q =time_spent_in_triage_q
    self.time_spent_while_triaging=time_spent_while_triaging
    self.total_time_spent=total_time_spent
    
#Schema for serialisation and desirialisation
class QueSimulationRunSchema(ma.Schema):
  class Meta:
    fields = ("id", "run_no", "patient_no", "time_spent_in_booking_q", 
    "time_spent_while_booking", "time_spent_in_triage_q","time_spent_while_triaging",
    "total_time_spent", "qsimulation_id")

#Schema objects for routes
que_simulation_run_schema= QueSimulationRunSchema()
que_simulation_runs_schema = QueSimulationRunSchema(many= True)
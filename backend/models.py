from backend import db, ma
import datetime



class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique= True, nullable = False)
    department_name = db.Column(db.String(200),nullable = False )
    #back ref for services
    services =db.relationship('Service', backref='department', cascade="all, delete-orphan")

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
  qsimulations = db.relationship('Simulation', backref='service', cascade="all, delete-orphan")

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
  #backref for Input
  input = db.relationship('Input', backref='simulation', cascade="all, delete-orphan")
  
  def __init__(self,simulation_name, service_id):
    self.simulation_name= simulation_name
    self.service_id =service_id

#Schema for serialisation and desirialisation
class SimulationSchema(ma.Schema):
  class Meta:
    fields = ("id", "simulation_name", "date", "service_id")

#Schema objects for routes
simulation_schema= SimulationSchema()
simulations_schema = SimulationSchema(many= True)




#QUESIMULATION MODEL
class Input(db.Model):
  #Columns
  id = db.Column(db.Integer, primary_key=True, nullable = False)
  warm_up_duration = db.Column(db.Float, nullable = False)
  total_duration =   db.Column(db.Float,  nullable = False )
  patient_interval_time = db.Column(db.Float, nullable = False)
  receptionist_no = db.Column(db.Integer, nullable = False)
  receptionist_booking_time= db.Column(db.Float, nullable = False)
  triager_no = db.Column(db.Integer, nullable = False)
  nurse_triage_time= db.Column(db.Float, nullable = False)
  iot_booking_time= db.Column(db.Float, nullable = False)
  iot_triage_time= db.Column(db.Float, nullable = False)
  control_delay = db.Column(db.Float, nullable = False)
  total_runs_no = db.Column(db.Integer, nullable = False)


  #Foreign key
  simulation_id = db.Column(db.Integer, db.ForeignKey('simulation.id'))
  Avg_output= db.relationship('AvgOutput', backref='input',  cascade="all, delete-orphan")
  #backref for QSimulationrun
  output= db.relationship('Output', backref='input', cascade="all, delete-orphan")
 


  def __init__(self, warm_up_duration,total_duration,total_runs_no,
  patient_interval_time,receptionist_no, receptionist_booking_time, triager_no, nurse_triage_time,
     iot_booking_time, iot_triage_time, control_delay, simulation_id):

   self.warm_up_duration= warm_up_duration
   self.total_duration =total_duration
   self.total_runs_no=total_runs_no
   self.patient_interval_time =patient_interval_time
   self.receptionist_no =receptionist_no
   self.receptionist_booking_time =receptionist_booking_time
   self.triager_no =triager_no
   self.nurse_triage_time= nurse_triage_time
   self.iot_booking_time=iot_booking_time
   self.iot_triage_time=iot_triage_time
   self.control_delay =control_delay
   self.simulation_id=simulation_id


#Schema for serialisation and desirialisation
class InputSchema(ma.Schema):
  class Meta:
    fields = ("id", "warm_up_duration","total_duration","total_runs_no",
    "patient_interval_time","receptionist_no", "receptionist_booking_time", "triager_no", "nurse_triage_time",
     "iot_booking_time",  "iot_triage_time", "control_delay", "simulation_id")

#Schema objects for routes
input_schema= InputSchema()
input_schemas = InputSchema(many= True)
   

#QueSimulationRun MODEL
class Output(db.Model):
   id = db.Column(db.Integer, primary_key=True,  nullable = False)
   run_no = db.Column(db.Integer, nullable = False)
   patient_no = db.Column(db.Integer, nullable = False)
   time_spent_in_booking_q = db.Column(db.Float)
   time_spent_while_booking = db.Column(db.Float)
   time_spent_in_triage_q= db.Column(db.Float)
   time_spent_while_triaging = db.Column(db.Float)
   total_time_spent = db.Column(db.Float)
   is_digital = db.Column(db.Boolean)

   #defining foreign key
   input_id= db.Column(db.Integer, db.ForeignKey('input.id'))
   
   def __init__(self,run_no,patient_no,time_spent_in_booking_q,  
   time_spent_while_booking,time_spent_in_triage_q, 
   time_spent_while_triaging,total_time_spent, is_digital, input_id):
    self.run_no =run_no
    self.patient_no=patient_no
    self.time_spent_in_booking_q =time_spent_in_booking_q
    self.time_spent_while_booking=time_spent_while_booking
    self.time_spent_in_triage_q =time_spent_in_triage_q
    self.time_spent_while_triaging=time_spent_while_triaging
    self.total_time_spent=total_time_spent
    self.is_digital=  is_digital
    self.input_id=input_id
    
#Schema for serialisation and desirialisation
class OutputSchema(ma.Schema):
  class Meta:
    fields = ("id", "run_no", "patient_no", "time_spent_in_booking_q", 
    "time_spent_while_booking", "time_spent_in_triage_q","time_spent_while_triaging",
    "total_time_spent", "is_digital","input_id")

#Schema objects for routes
output_schema= OutputSchema()
output_schemas = OutputSchema(many= True)

#OUTPUT2 MODEL 
class AvgOutput(db.Model):
   id = db.Column(db.Integer, primary_key=True,  nullable = False)
   run_no = db.Column(db.Integer, nullable = False)
   total_patient_no = db.Column(db.Integer, nullable = False)
   avg_total_time_spent = db.Column(db.Float)
   is_digital = db.Column(db.Boolean)
   #defining foreign key
   input_id= db.Column(db.Integer, db.ForeignKey('input.id'))
   
   def __init__(self,run_no,total_patient_no,avg_total_time_spent, is_digital, input_id):
    self.run_no =run_no
    self.total_patient_no =total_patient_no
    self.avg_total_time_spent =avg_total_time_spent
    self.is_digital=is_digital
    self.input_id=input_id
    
#Schema for serialisation and desirialisation
class AvgOutputSchema(ma.Schema):
  class Meta:
    fields = ("id", "run_no", "total_patient_no", "avg_total_time_spent", "is_digital", "input_id")

#Schema objects for routes
avg_output_schema= AvgOutputSchema()
avg_output_schemas = AvgOutputSchema(many= True)




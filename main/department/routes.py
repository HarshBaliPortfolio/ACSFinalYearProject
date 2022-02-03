from flask import jsonify, request
from simulation import EDQModel
from . import department
from models import db, Department, department_schema, departments_schema, Service, service_schema, services_schema, Simulation, simulation_schema, simulations_schema, QueSimulation, QueSimulationRun, que_simulation_run_schema, que_simulation_runs_schema, que_simulation_schema,que_simulations_schema









#DEPARTMENT

#add department
@department.route('/', methods =['POST'])
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
@department.route('/', methods =['GET'])
def list_departments():
  #fetch all departments from mysql
  all_department = Department.query.all()
  # dump the results into department schema and serilise/deserialise it
  list_departments = departments_schema.dump(all_department)
  return jsonify(list_departments)

# get department by id 
@department.route('/<id>/', methods =['GET'])
def get_department(id):
    #Query db
  department = Department.query.get(id)
    #return the jsonify in schema
  return department_schema.jsonify(department)

#update
@department.route('/update/<id>/', methods =['PUT'])
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

#delete
@department.route('/delete/<id>/', methods =['DELETE'])
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









#SERVICE
#SERVICE
#GET
@department.route('/<id>/services', methods =['GET'])
def get_services(id):
  all_services_of_department = Service.query.filter_by(department_id=id).all()

  list_services=services_schema.dump(all_services_of_department)
  return jsonify(list_services)

#ADD
@department.route('/<id>/services', methods =['POST'])
def add_service(id):
  service_name = request.json['service_name']
  service = Service(service_name, id)
  # adding to db
  db.session.add(service)
  db.session.commit()
  # returning jsonify of 1 department
  return service_schema.jsonify(service)

#DELETE
@department.route('/services/delete/<service_id>', methods =['DELETE'])
def delete_service(service_id):
  #GET DEP
  service = Service.query.get(service_id)
  #del it and commit
  db.session.delete(service)
  db.session.commit()
  #jsonify it
  return service_schema.jsonify(service)










#SIMULATION
#SIMULATION
# SHOW LIST
@department.route('/service/<service_id>/simulations', methods =['GET'])
def get_simulations(service_id):
  all_simulations_of_a_service = Simulation.query.filter_by(service_id=service_id).all()

  list_simulations=simulations_schema.dump(all_simulations_of_a_service)
  return jsonify(list_simulations)

#ADD
@department.route('/service/<service_id>/simulations', methods =['POST'])
def add_simulation(service_id):
  simulation_name = request.json['simulation_name']
  simulation = Simulation(simulation_name, service_id)
  # adding to db
  db.session.add(simulation)
  db.session.commit()

  # fetch all the data from db where service id = service id 
  all_simulations_of_a_service = Simulation.query.filter_by(service_id=service_id).all()
  list_simulations=simulations_schema.dump(all_simulations_of_a_service)

  return jsonify(list_simulations)
 

@department.route('/simulation/delete/<id>/', methods =['DELETE'])
def delete_simulation(id):
  #GET DEP
  simulation = Simulation.query.get(id)
  #getting foreign key before deletion
  foreign_id = simulation.service_id
  #del it and commit
  db.session.delete(simulation)
  db.session.commit()
  all_simulations = Simulation.query.filter_by(service_id=foreign_id).all()
  #dump all dep in dep schema
  list_simulations = simulations_schema.dump(all_simulations)
  #jsonify it
  return jsonify(list_simulations)














#QueSimulation
#QueSimulation

#get q simulations
@department.route('/simulation/<simulation_id>/que', methods =['GET'])
def get_que_simulation(simulation_id):
  all_que_simulations_of_a_simulation = QueSimulation.query.filter_by(simulation_id=simulation_id).all()

  list_que_simulations=que_simulations_schema.dump(all_que_simulations_of_a_simulation)
  return jsonify(list_que_simulations)

#add q simulation
@department.route('/simulation/<simulation_id>/que/', methods =['POST'])
def add_que_simulation(simulation_id):

  warm_up_duration= request.json['warm_up_duration']
  total_duration = request.json['total_duration']
  patient_interval_time = request.json['patient_interval_time']
  receptionist_booking_time = request.json['receptionist_booking_time']
  nurse_triage_time = request.json['nurse_triage_time']
  receptionist_no = request.json['receptionist_no']
  triage_nurse_no = request.json['triage_nurse_no']
  iot_booking_time = 0.0
  iot_triage_time = 0.0
  booking_iot_no = 0.0
  triage_iot_no = 0.0
  total_runs_no = request.json['total_runs_no']

  que_simulation = QueSimulation(warm_up_duration,total_duration,total_runs_no,
  patient_interval_time,receptionist_no, receptionist_booking_time, triage_nurse_no, nurse_triage_time,
    booking_iot_no, iot_booking_time, triage_iot_no,  iot_triage_time, simulation_id)

 
  # adding to db
  db.session.add(que_simulation)
  db.session.commit()

  
 #run the simulation for total_runs_no
  for run in range(total_runs_no):
    print("Run ", run + 1, " from ", total_runs_no, sep="")
    #pass other values to emergency department que model
    run_simu =  EDQModel(warm_up_duration,total_duration,run,
    patient_interval_time,receptionist_no, receptionist_booking_time, triage_nurse_no, nurse_triage_time,
    booking_iot_no, iot_booking_time, triage_iot_no,  iot_triage_time,simulation_id)
    run_simu.run()
    print()

  # fetch all the data from db
  all_que_simulations_of_a_simulation = QueSimulation.query.filter_by(simulation_id=simulation_id).all()
  list_que_simulations=que_simulations_schema.dump(all_que_simulations_of_a_simulation)

  return jsonify(list_que_simulations)





#add q simulation
@department.route('/simulation/<simulation_id>/que/digital', methods =['POST'])
def add_que_simulation_for_digital(simulation_id):

  warm_up_duration= request.json['warm_up_duration']
  total_duration = request.json['total_duration']
  patient_interval_time = request.json['patient_interval_time']
  receptionist_booking_time = 0.0
  nurse_triage_time = 0.0
  receptionist_no = 0.0
  triage_nurse_no = 0.0
  iot_booking_time = request.json['iot_booking_time']
  iot_triage_time = request.json['iot_triage_time']
  booking_iot_no = request.json['booking_iot_no']
  triage_iot_no = request.json['triage_iot_no']
  total_runs_no = request.json['total_runs_no']

  que_simulation = QueSimulation(warm_up_duration,total_duration,total_runs_no,
  patient_interval_time,receptionist_no, receptionist_booking_time, triage_nurse_no, nurse_triage_time,
    booking_iot_no, iot_booking_time, triage_iot_no,  iot_triage_time, simulation_id)

 
  # adding to db
  db.session.add(que_simulation)
  db.session.commit()

  
 #run the simulation for total_runs_no
  for run in range(total_runs_no):
    print("Run ", run + 1, " from ", total_runs_no, sep="")
    #pass other values to emergency department que model
    run_simu =  EDQModel(warm_up_duration,total_duration,run,
    patient_interval_time,receptionist_no, receptionist_booking_time, triage_nurse_no, nurse_triage_time,
    booking_iot_no, iot_booking_time, triage_iot_no,  iot_triage_time,simulation_id)
    run_simu.run()
    print()



  #fetch all the data from db
  all_que_simulations_of_a_simulation = QueSimulation.query.filter_by(simulation_id=simulation_id).all()
  list_que_simulations=que_simulations_schema.dump(all_que_simulations_of_a_simulation)

  return jsonify(list_que_simulations)






#Delete q simulation
@department.route('/simulation/que/<id>', methods =['DELETE'])
def delete_que_simulation(id):

  #GET que
  que_simulation = QueSimulation.query.get(id)
  #getting foreign key before deletion
  foreign_id = que_simulation.simulation_id
  #del it and commit
  db.session.delete(que_simulation)
  db.session.commit()
  
  all_que_simulations_of_a_simulation = QueSimulation.query.filter_by(simulation_id=foreign_id).all()
  list_que_simulations=que_simulations_schema.dump(all_que_simulations_of_a_simulation)

  return jsonify(list_que_simulations)







#QueSimulationRun
#QueSimulationRun 
#get simulation runS
@department.route('/que/<que_simulation_id>/queruns', methods =['GET'])
def get_que_simulation_run(que_simulation_id):
  all_runs_of_a_simulation = QueSimulationRun.query.filter_by(que_simulation_id=que_simulation_id).all()

  list_runs=que_simulation_runs_schema.dump(all_runs_of_a_simulation)
  return jsonify(list_runs)
  

#Delete simulation
@department.route('/que/querun/<id>', methods =['DELETE'])
def delete_que_simulation_run(id):
  que_simulation_run = QueSimulationRun.query.get(id)
  foreign_id = que_simulation_run.que_simulation_id

  db.session.delete(que_simulation_run)
  db.session.commit()
  
  all_runs_of_simulation = QueSimulationRun.query.filter_by(simulation_id=foreign_id).all()
  list_que_runs=que_simulation_runs_schema.dump(all_runs_of_simulation)
  return jsonify(list_que_runs)






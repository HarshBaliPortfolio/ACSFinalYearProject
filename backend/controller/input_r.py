from flask import Blueprint, request, jsonify
from .. import db
from  backend.models import Input, input_schema, input_schemas
import time


# importing simulation 
import backend.b_t_service.simulation as simulation

input = Blueprint("input", __name__)
#GET

#get simulation inputs
@input.route('/<simulation_id>/inputs', methods =['GET'])
def get_que_simulation(simulation_id):
  all_que_simulations_of_a_simulation = Input.query.filter_by(simulation_id=simulation_id).all()

  list_que_simulations=input_schemas.dump(all_que_simulations_of_a_simulation)
  return jsonify(list_que_simulations)








#add input to simulation
@input.route('/<simulation_id>/input', methods =['POST'])
def add_que_simulation(simulation_id):
  start = time.time()
  warm_up_duration= request.json['warm_up_duration']
  total_duration = request.json['total_duration']
  patient_interval_time = request.json['patient_interval_time']
  receptionist_booking_time = request.json['receptionist_booking_time']
  nurse_triage_time = request.json['nurse_triage_time']
  receptionist_no = request.json['receptionist_no']
  triager_no = request.json['triager_no']
  iot_booking_time =request.json['iot_booking_time']
  iot_triage_time =request.json['iot_triage_time']
  control_delay = request.json['control_delay']
  total_runs_no = request.json['total_runs_no']

  input = Input(warm_up_duration,total_duration,total_runs_no,
  patient_interval_time,receptionist_no, receptionist_booking_time, triager_no,
   nurse_triage_time,
   iot_booking_time,  iot_triage_time, control_delay,  simulation_id)

  # adding to db
  db.session.add(input) 
  db.session.commit()
  db.session.refresh(input)


  input_id = input.id

# As-is service
  for run in range(int(total_runs_no)):
    # print("Run ", run + 1, " from ", total_runs_no, sep="")
    #pass other values to emergency department que model
    
    run_simu =  simulation.EDQModel(warm_up_duration,total_duration,run,
    patient_interval_time,receptionist_no, receptionist_booking_time, triager_no,  nurse_triage_time,
    iot_booking_time,  iot_triage_time, control_delay,  False, input_id)
    run_simu.run()
    run_simu.add_avg_output()
    # print()

 # Digital service
  for run in range(int(total_runs_no)):
    # print("Run ", run + 1, " from ", total_runs_no, sep="")
    #pass other values to emergency department que model
    
    run_simu =  simulation.EDQModel(warm_up_duration,total_duration,run,
    patient_interval_time,receptionist_no, receptionist_booking_time, triager_no, nurse_triage_time,
    iot_booking_time,  iot_triage_time,control_delay, True,input_id)
    run_simu.run()
    run_simu.add_avg_output()
    # print()

  finish = time.time()
  timeTaken= finish -start
  #print the time taken
  print()
  print("Simulation duration input:", total_duration, " time taken:", timeTaken)
  print()
  return input_schema.jsonify(input)





# #Delete q simulation
@input.route('/record/<id>', methods =['DELETE'])
def delete_que_simulation(id):

  #GET que
  input = Input.query.get(id)
  #getting foreign key before deletion
  foreign_id = input.simulation_id
  #del it and commit
  db.session.delete(input)
  db.session.commit()
  
  all_que_simulations_of_a_simulation = Input.query.filter_by(simulation_id=foreign_id).all()
  list_que_simulations= input_schemas.dump(all_que_simulations_of_a_simulation)

  return jsonify(list_que_simulations)





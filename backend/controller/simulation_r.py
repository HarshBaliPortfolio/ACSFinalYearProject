from flask import Blueprint, request, jsonify
from .. import db
from  backend.models import Simulation, SimulationSchema, simulations_schema

simulation = Blueprint("simulation", __name__)




# SHOW LIST
@simulation.route('/<service_id>/simulations', methods =['GET'])
def get_simulations(service_id):
  all_simulations_of_a_service = Simulation.query.filter_by(service_id=service_id).all()

  list_simulations=simulations_schema.dump(all_simulations_of_a_service)
  return jsonify(list_simulations)

#ADD
@simulation.route('/<service_id>/simulation', methods =['POST'])
def add_simulation(service_id):
  simulation_name = request.json['simulation_name']
  simulation = Simulation(simulation_name, service_id)
  # adding to db
  db.session.add(simulation)
  db.session.commit()

  # fetch all the data from db where service id = service id 
  all_simulations_of_a_service = Simulation.query.filter_by(service_id=service_id).all()
  list_simulations=simulations_schema.dump(all_simulations_of_a_service)

  #Return view of simulations
  return jsonify(list_simulations)
 

@simulation.route('/simulation/delete/<id>/', methods =['DELETE'])
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

from flask import Blueprint, request, jsonify
from backend import  db
from backend.models import output_schema, Output, output_schemas

output = Blueprint("output", __name__)


# #QueSimulationRun 
# #get simulation runS
@output.route('/<input_id>/outputs', methods =['GET'])
def get_que_simulation_run(input_id):
  output = Output.query.filter_by(input_id=input_id).all()

  list_runs= output_schemas.dump(output)
  return jsonify(list_runs)
  

# #Delete simulation
@output.route('/output/<id>', methods =['DELETE'])
def delete_que_simulation_run(id):
  output = Output.query.get(id)
  foreign_id = output.input_id

  db.session.delete(output)
  db.session.commit()
  
  all_output = Output.query.filter_by(simulation_id=foreign_id).all()
  list_que_runs= output_schemas.dump(all_output)
  return jsonify(list_que_runs)

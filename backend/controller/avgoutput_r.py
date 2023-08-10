from flask import Blueprint, request, jsonify
from backend import db
from backend.models import  avg_output_schema, AvgOutput, avg_output_schemas



avgoutput = Blueprint("avgoutput", __name__)


 
# get avg output
@avgoutput.route('/<input_id>/avg/outputs', methods =['GET'])
def get_avg_output(input_id):
  #get avg output by id
  output = AvgOutput.query.filter_by(input_id=input_id).all()

  list_runs= avg_output_schemas.dump(output)

  #return the output as json object
  return jsonify(list_runs)
  





# #Delete simulation
@avgoutput.route('/avg/output/<id>', methods =['DELETE'])
def delete_avg_output(id):
  que_simulation_run = AvgOutput.query.get(id)
  foreign_id = que_simulation_run.que_simulation_id

  db.session.delete(que_simulation_run)
  db.session.commit()
  
  all_output = AvgOutput.query.filter_by(simulation_id=foreign_id).all()
  list_que_runs= avg_output_schemas.dump(all_output)
  return jsonify(list_que_runs)
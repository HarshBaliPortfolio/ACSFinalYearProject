from flask import Blueprint, request, jsonify
from .. import db
from backend.models import Department, department_schema,departments_schema

department = Blueprint("department", __name__)


#add department
@department.route('/department', methods =['POST'])
def add_department():
  #fetching the input from user
  print(request.json)
  department_name = request.json['department_name']

  #creating a model and passing the input
  department = Department(department_name)
  # adding to db
  db.session.add(department)
  db.session.commit()
  # returning jsonify view of department
  return department_schema.jsonify(department)

# get list of departments
@department.route('/departments', methods =['GET'])
def list_departments():
  #fetch all departments from mysql
  all_department = Department.query.all()
  # dump the results into department schema and serilise/deserialise it
  list_departments = departments_schema.dump(all_department)
  return jsonify(list_departments)

# get department by id 
@department.route('/<id>/department', methods =['GET'])
def get_department(id):
    #Query db
  department = Department.query.get(id)
    #return the jsonify in schema
  return department_schema.jsonify(department)

# #update
# @department.route('/department/update/<id>', methods =['PUT'])
# def update_department(id):
#   department = Department.query.get(id)
#   #get the new value
#   department_name = request.json['department_name']
#   #the previous value = new value
#   department.department_name = department_name
#   #commit the change
#   db.session.commit()
#   #return the update 
#   return department_schema.jsonify(department)

#delete
@department.route('/department/delete/<id>', methods =['DELETE'])
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


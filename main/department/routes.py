from flask import jsonify, request
from . import department
from models import db, Department, department_schema, departments_schema, Service, service_schema, services_schema

#TODO: on adding, more than 1 should be returned


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

#gets all services with department
@department.route('/<id>/services', methods =['GET'])
def get_services(id):
  all_services_of_department = Service.query.filter_by(department_id=id).all()

  list_services=services_schema.dump(all_services_of_department)
  return jsonify(list_services)

@department.route('/<id>/services', methods =['POST'])
def add_service(id):
  service_name = request.json['service_name']
  service = Service(service_name, id)
  # adding to db
  db.session.add(service)
  db.session.commit()
  # returning jsonify of 1 department
  return service_schema.jsonify(service)

@department.route('/services/<service_id>/delete/', methods =['DELETE'])
def delete_service(service_id):
  #GET DEP
  service = Service.query.get(service_id)
  #del it and commit
  db.session.delete(service)
  db.session.commit()
  #jsonify it
  return service_schema.jsonify(service)


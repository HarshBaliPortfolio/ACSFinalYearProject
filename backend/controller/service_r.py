from flask import Blueprint, request, jsonify
from .. import db
from  backend.models import Service, service_schema, services_schema

service = Blueprint("service", __name__)
#GET
@service.route('/<id>/services', methods =['GET'])
def get_services(id):
  all_services_of_department = Service.query.filter_by(department_id=id).all()

  list_services=services_schema.dump(all_services_of_department)
  return jsonify(list_services)

#ADD
@service.route('/<department_id>/service', methods =['POST'])
def add_service(department_id):
  service_name = request.json['service_name']
  service = Service(service_name, department_id)
  # adding to db
  db.session.add(service)
  db.session.commit()
  # returning jsonify of service
  return service_schema.jsonify(service)

#DELETE
@service.route('/service/delete/<service_id>', methods =['DELETE'])
def delete_service(service_id):
  #GET DEP
  service = Service.query.get(service_id)
  #del it and commit
  db.session.delete(service)
  db.session.commit()
  #jsonify it
  return service_schema.jsonify(service)




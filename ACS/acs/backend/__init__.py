#from main import app
import imp
from flask import Flask 
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS





# TODO warmup period in **simulation module**
    # TODO record the **input/output data** in csv file
#TODO: in future might need bussiness logic for data visualisation
    #TODO: update routes for visualisation



# Tell python we r creating flask web app
app = Flask(__name__)
CORS(app)




#Link it here  mysql://root:password@localhost/database name'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:@localhost/'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

#marshmallow obj for serialisation
ma = Marshmallow(app)
db = SQLAlchemy(app)

@app.errorhandler(404)
def handle_error(e):
    return "EndPoint does not exist"

@app.errorhandler(500)
def handle_error(e):
    return "The post request contents are invalid"

    
#registers blueprint or informs the route
from .controller.department_r import department
app.register_blueprint(department, url_prefix="/")


from .controller.service_r import service
app.register_blueprint(service, url_prefix="/department")

from .controller.simulation_r import simulation
app.register_blueprint(simulation, url_prefix="/service")

#TODO: change the link 
from .controller.input_r import input
app.register_blueprint(input, url_prefix="/simulation")

#TODO: change the link 
from .controller.output_r import output
app.register_blueprint(output, url_prefix="/input")

from .controller.avgoutput_r import avgoutput
app.register_blueprint(avgoutput, url_prefix="/input")






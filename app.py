import email
from flask import Flask
#routes is in different package
from routes.routes import welcome
from flask_sqlalchemy import SQLAlchemy


# Tell python we r creating flask web app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:Bali!997@localhost/simulation_data'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False'

#registers blueprint or informs the route
app.register_blueprint(welcome)

# instanciate sqlalchemy
db = SQLAlchemy(app)

# creates a table for the schema
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __init__(self, username):
      self.username=username
      self.email=email




# run the app in dev mode
if __name__ == "__main__":
    app.run(debug=True)
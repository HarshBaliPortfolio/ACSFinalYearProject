import email
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


#Tell python we r creating flask web app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:Bali!997@localhost/simulation_data'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False'


db = SQLAlchemy(app)
#db = SQLAlchemy(app)


#creates table for the schema
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __init__(self, username):
      self.username=username
      self.email=email

  



# mapping method/function to http request
@app.route("/get", methods =['GET'])
def hello_world():
    return jsonify({"hello":"flask!"})


if __name__ == "__main__":
    app.run(debug=True)
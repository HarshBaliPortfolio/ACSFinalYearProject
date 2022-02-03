from main import app



# TODO warmup period in **simulation module**
    # TODO record the **input/output data** in csv file
#TODO: in future might need bussiness logic for data visualisation
    #TODO: update routes for visualisation




   



from models import db
db.create_all()

# run the app in dev mode
if __name__ == "__main__":
    app.run()
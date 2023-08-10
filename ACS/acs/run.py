from backend import app, db

db.create_all()
# 
# To run the system
# Pls Create a MYSQL database 
# and link it with the project in  __init__ file in backend







# run the app in dev mode
if __name__ == "__main__":
    app.run()
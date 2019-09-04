import requests
import time 
import sqlalchemy as db


config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'rise',
    'database': 'timings-server'
}
dbuser = config.get('user')
dbhost = config.get('host')
dbport = config.get('port')
dbpass = config.get('password')
dbname = config.get('database')

connection_str = f"mysql+pymysql://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbname}"
# connect to db
engine = db.create_engine(connection_str)
conn = engine.connect()





start = time.time()
ip = "http://localhost:5000/new"
params = {"q":800, "length":250}

def testing():
    for i in range(320):
        req = requests.get(ip, params=params)
    return True

def add():
    pass

if __name__ == "__main__":
    if testing() == True:
        end = time.time()
        duration = end - start
        print(f"DONE in {duration}")



            
    


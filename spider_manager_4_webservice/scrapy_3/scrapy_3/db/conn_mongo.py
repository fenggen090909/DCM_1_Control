
import logging
from pymongo import MongoClient

class ConnectionDBMongo:
    
    def __init__(self, db_name, collection_name):     

        logging.critical(f"fenggen conn_mongo ConnectionDBPostgres __init__ 10")

        try:
            client = MongoClient("mongodb://fenggen090909:Fg285426*@192.168.0.58:27017/")
            db = client[db_name]
            self.collection = db[collection_name]
            logging.critical(f"fenggen get db and collection")
            

        except Exception as e:
            logging.critical(f"fenggen mongo.connect error {e}")
        
        

    

        





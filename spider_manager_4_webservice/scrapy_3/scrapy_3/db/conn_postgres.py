from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging
import contextlib

class ConnectionDBPostgres:
    
    def __init__(self, db_name):     

        logging.critical(f"fenggen conn_postgres ConnectionDBPostgres __init__ 10")
        
        if db_name == "questionshunt":
            try:                
                self.engine_questionshunt = create_engine(f"postgresql://postgres:Fg285426*@192.168.0.58:5432/questionshunt")            
                with self.engine_questionshunt.connect() as conn:
                    pass

            except Exception as e:
                logging.critical(f"fenggen engine_questionshunt.connect error {e}")        
            
            self.session_questionshunt = sessionmaker(bind=self.engine_questionshunt)
        
        if db_name == "kaggle":
            try:                
                self.engine_kaggle = create_engine(f"postgresql://postgres:Fg285426*@192.168.0.58:5432/kaggle")            
                with self.engine_kaggle.connect() as conn:
                    pass

            except Exception as e:
                logging.critical(f"fenggen engine_kaggle.connect error {e}")        
            
            self.session_kaggle = sessionmaker(bind=self.engine_kaggle) 

    @contextlib.contextmanager
    def session_scope(self, db_name):
        
        if db_name == "questionshunt":
            session_questionshunt = self.session_questionshunt()
            try:
                yield session_questionshunt
                session_questionshunt.commit()
            except:
                session_questionshunt.rollback()
                raise
            finally:
                session_questionshunt.close() 

        if db_name == "kaggle":
            session_kaggle = self.session_kaggle()
            try:
                yield session_kaggle
                session_kaggle.commit()
            except:
                session_kaggle.rollback()
                raise
            finally:
                session_kaggle.close()    

        





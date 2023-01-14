import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os


# To use this functionality fill in the details in env_variables.sh
# and then use `source env_variables.sh` before starting the poetry app. 
# Note that env_variables.sh is included in the gitignore file. 
# In production the environment variables should be set in a different way. 

class DatabaseConnector():
    def __init__ (self):
        pass

    @st.experimental_singleton
    def get_db_sessionmaker(_self):
        # These may need adjusting depending on database settings
        WAREHOUSE_USERNAME=os.environ['WAREHOUSE_USERNAME']
        WAREHOUSE_PASSWORD=os.environ['WAREHOUSE_PASSWORD']
        HOST=os.environ['HOST']
        DB_PORT=os.environ['DB_PORT']
        WAREHOUSE_NAME=os.environ['WAREHOUSE_NAME']
        SSL_MODE=os.environ['SSL_MODE']
    
        SQLALCHEMY_DATABASE_URL = f"postgresql://{WAREHOUSE_USERNAME}:{WAREHOUSE_PASSWORD}@{HOST}:{DB_PORT}/{WAREHOUSE_NAME}?sslmode={SSL_MODE}"

        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        Session = sessionmaker(bind=engine)
        return Session()

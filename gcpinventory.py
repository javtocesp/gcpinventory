import os
from sqlalchemy import create_engine, MetaData

USER_DB=os.environ['USER_DB']
PASS_DB=os.environ['PASS_DB']
NAME_DB=os.environ['NAME_DB']
PORT_DB=os.environ['PORT_DB']

def connect_db():
    engine = create_engine("mysql+pymysql://{}:{}@{}:{}".format(USER_DB,PASS_DB,NAME_DB,PORT_DB))
    conn = engine.connect()
    return conn

    
import pymysql
from app.config import db_config

def get_db_connection():
    connection = pymysql.connect(
        host=db_config['host'],
        port=db_config['port'], 
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )
    return connection
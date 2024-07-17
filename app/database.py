import pymysql
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

def get_db_connection():
    
    connection = pymysql.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return connection





""" import pymysql
from app.config import db_config

def get_db_connection():
    connection = pymysql.connect(
        host=db_config['host'],
        port=db_config['port'], 
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )
    return connection """
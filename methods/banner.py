import os, sqlalchemy, oracledb, sys

from methods.password_decrypt import password_decryptor
from dotenv import load_dotenv
from sqlalchemy.exc import SQLAlchemyError
from loguru import logger as log

# Run some stuff here to make oracldb work
oracledb.version = "8.3.0"
sys.modules["cx_Oracle"] = oracledb

#Written by Logan Burkham

#Loads .env into OS
load_dotenv()
BAN_DB_URL = os.getenv('BAN_DB_URL')
BAN_DB_USER = os.getenv('BAN_DB_USER')
BAN_DB_PORT = os.getenv('BAN_DB_PORT')
BAN_DB_SERVICE_NAME = os.getenv('BAN_DB_SERVICE_NAME')
BAN_DB_PASSWORD = os.getenv('BAN_DB_PASSWORD')
BAN_DB_REFKEY = os.getenv('BAN_DB_REFKEY')
BAN_DIALECT = os.getenv('BAN_DIALECT')

PASSWORD = (password_decryptor(BAN_DB_PASSWORD, BAN_DB_REFKEY)).get_pwrd()
# GLOBAL SQLAlchemy engine connector string object
ENGINE_PATH_WIN_AUTH = f'{BAN_DIALECT}://{BAN_DB_USER}:{PASSWORD}@{BAN_DB_URL}:{BAN_DB_PORT}/{BAN_DB_SERVICE_NAME}'

# The class is used to connect to a remote database and a local database.
class database:
    _instance = None
    conn = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(database, cls).__new__(cls, *args, **kwargs)
            try:
                # Create a connection object for the remote database
                cls._instance.conn = sqlalchemy.create_engine(ENGINE_PATH_WIN_AUTH, arraysize=1000)
                log.info(f"Connected to {BAN_DB_URL}: Banner Connection: {cls._instance.conn}")
            except SQLAlchemyError as e:
                log.error(e)
        return cls._instance

    # Close the db connection
    def quit(self):
        try:
            if self.conn is not None:
                self.conn.dispose()
                log.info(f"Closed connection to {BAN_DB_URL}")
            else:
                log.warning("Connection is not initialized.")
        except Exception as e:
            log.error(f"Unable to close connection to {BAN_DB_URL}: {e}")
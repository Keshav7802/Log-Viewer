# config.py

# Edit the DB_USERNAME, DB_PASSWORD, etc for the successful access of the database
# A user can create a database named 'november_2023_hiring_Keshav7802' in the specified DB_HOST.

DB_USERNAME = 'root'
DB_PASSWORD = 'keshav7802'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'november_2023_hiring_Keshav7802'

SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

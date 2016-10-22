import mysql.connector

config = {'user':'openpet',
          'password':'openpet',
          'host':'127.0.0.1',
          'database':'openpet'}

def get_connection():
    connection = mysql.connector.connect(**config)
    return connection

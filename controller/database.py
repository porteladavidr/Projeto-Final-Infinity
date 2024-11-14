import pyodbc

server = 'DAVID\\SQLEXPRESS'
database = 'INDUSTRIA_WAYNE'
username = 'wayne'
password = 'batman'

connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

def get_connection():
    return pyodbc.connect(connection_string)

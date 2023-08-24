import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Sebs123!')

cursorObj = database.cursor()

cursorObj.execute("CREATE DATABASE expertoon")

print("Database created.")
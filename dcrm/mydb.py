import mysql.connector

dataBAse = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mecoSQL27'
)

# prepare a cursor object
cursorObject = dataBAse.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("ALL Done!")
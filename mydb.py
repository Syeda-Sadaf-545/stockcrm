import mysql.connector

from mysql.connector import (connection)

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='admin',
    auth_plugin='mysql_native_password'
)


# Prepare a cursor-object
cursorObject = dataBase.cursor()
# create a database
cursorObject.execute("CREATE DATABASE stockcrmdb")
print("All Done Successfully!")

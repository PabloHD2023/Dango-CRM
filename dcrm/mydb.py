import pymysql
pymysql.install_as_MySQLdb()
import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Admin12345",
)

cursorObject = dataBase.cursor()
#

cursorObject.execute("CREATE DATABASE IF NOT EXISTS dcrm_db")
#
print("Database created successfully")
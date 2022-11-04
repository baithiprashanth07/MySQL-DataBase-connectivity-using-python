import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database="mydatabase",
  user="root",
  password="1234"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

import mysql.connector
conn= mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)

mycursor = conn.cursor()

mycursor.execute("CREATE DATABASE employee2")
mycursor.close()
conn.close()


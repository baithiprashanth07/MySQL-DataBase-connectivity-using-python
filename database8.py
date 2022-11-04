import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database="mydatabase",
  user="root",
  password="1234"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()


for x in myresult:
  print(x)

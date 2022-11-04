import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database="mydatabase",
  user="root",
  password="1234"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

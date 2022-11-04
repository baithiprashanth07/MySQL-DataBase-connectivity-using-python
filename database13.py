import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database="mydatabase",
  user="root",
  password="1234"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

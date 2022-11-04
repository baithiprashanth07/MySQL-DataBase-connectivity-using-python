from mysql import connector
import mysql.connector
mydb=mysql.connector.connect(host='localhost',database='world',user='root',password='1234')
cursor=mydb.cursor()
cursor.execute("select * from emptab")
row= cursor.fetchone()
while row is not None:
    print(row)
    row=cursor.fetchone()
cursor.close()
mydb.close()

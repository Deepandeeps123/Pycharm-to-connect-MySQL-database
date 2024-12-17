import mysql.connector
mydb=mysql.connector.connect(
     host="Localhost",
     port="3306",
     user="root",
     password="python",
     database="python1"
)
a=mydb.cursor()
query=("create table emp ("
       "empno ")
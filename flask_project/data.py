from flask import Flask 
import mysql.connector
app = Flask(__name__)
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="YES"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

if __name__ == "__main__":
    app.run()

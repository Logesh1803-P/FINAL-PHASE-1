from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# configure MySQL
mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     password="1803",
     database="mydatabase"
)
# try:
#     mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="1803",
#     database="mydatabase"
#   )
#     print("connction seccess")
# except: 
#     print("some error") 

# create table if not exists
mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # insert username and password into database
    mycursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    mydb.commit()
    
    return "Login successful"

if __name__ == '__main__':
    app.run(debug=True)

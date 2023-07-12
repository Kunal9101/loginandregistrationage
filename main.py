from flask import Flask , render_template , request,redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)


app.secret_key = 'Kunal@9101'
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Admin@123'
app.config['MYSQL_DB'] = 'logininfo'
 
mysql = MySQL(app)

@app.route('/' ,methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password= request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM login WHERE email = %s AND  password= %s' , (email , password))
        account = cur.fetchone()
        cur.close()
        if account :
            return redirect(url_for('homepage'))
        else :
            return redirect(url_for('login'))


    return render_template("login.html")
    

@app.route('/reg' , methods = ['POST' ,'GET'])
def registration():
    if request.method == "POST":
        firstname = request.form['firstname']
        lastname  = request.form['lastname']
        email = request.form['email']
        password= request.form['password']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO login (firstname , lastname, email, password) VALUES (%s , %s, %s , %s)', (firstname , lastname, email ,password))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('login'))


    return render_template ("registration.html")   

@app.route('/home')
def homepage():
    return render_template ("home.html")  

if __name__ == "__main__":
    app.run(debug= True)

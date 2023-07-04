from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="system1234",
  database="mydb"  
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        college = request.form['college']
        # Insert the form data into the database
        cursor = db.cursor()
        sql = "INSERT INTO records (name, college) VALUES (%s, %s)"
        val = (name, college)
        cursor.execute(sql, val)
        db.commit()

    # Fetch all the submitted form data
    cursor = db.cursor()
    cursor.execute("SELECT * FROM records")
    data = cursor.fetchall()

    return render_template('index.html', data=data)

if __name__ == '_main_':
    app.run(debug=True)
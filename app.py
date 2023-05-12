
import mysql.connector
import os
from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)

USERNAME = os.environ.get("SQL_USERNAME")
PASSWORD = os.environ.get("SQL_PASSWORD")
SQL_SERVER = os.environ.get("SQL_SERVER")
SQL_DB = os.environ.get("SQL_DB")
TABLE_NAME = os.environ.get("TABLE_NAME")

def add_subscribers(name, email):
    connection = mysql.connector.connect(
        user=f"{USERNAME}@{SQL_SERVER}",
        password=PASSWORD,
        host=f"{SQL_SERVER}.mysql.database.azure.com",
        port=3306,
        database=SQL_DB,
        ssl_ca="cert.pem",
    )
    
    insert_subscribers_query = f"INSERT INTO {TABLE_NAME} (name, email) VALUES (%s,%s)"
    
    with connection.cursor() as cursor:
        cursor.execute(insert_subscribers_query, (name, email))
        connection.commit()
    print("Newsletter subscriber inserted successfully")


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    form_data = request.form
    name = form_data['name']
    email = form_data['email']
    
    add_subscribers(name=name, email=email)
    return redirect(url_for('/'))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
    
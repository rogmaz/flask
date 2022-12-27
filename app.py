from flask import Flask, render_template
import pymysql

app = Flask(__name__)
app.static_folder = 'static'


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='rogmaz',
                             password='rogmaz',
                             db='database')

@app.route('/')
def index():
    # Retrieve data from the database
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM users'
        cursor.execute(sql)
        result = cursor.fetchall()
    return render_template('index.html', data=result)

if __name__ == '__main__':
    app.run()

from flask import Flask, request, jsonify
import pymysql.cursors
from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB_NAME

app = Flask(__name__)

# Establish connection to MySQL database
connection = pymysql.connect(
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DB_NAME,
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/example1/user/<int:id>', methods=['GET'])
def example1(id):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE id=%s"
            cursor.execute(sql, (id,))
            result = cursor.fetchall()
            return jsonify(result)
    except Exception as e:
        return str(e), 500

@app.route('/example2/user/<int:id>', methods=['GET'])
def example2(id):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE id=%s"
            cursor.execute(sql, (id,))
            result = cursor.fetchall()
            return jsonify(result)
    except Exception as e:
        return str(e), 500

@app.route('/example3/user/<int:id>', methods=['GET'])
def example3(id):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE id=%s"
            cursor.execute(sql, (id,))
            result = cursor.fetchall()
            return jsonify(result)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)

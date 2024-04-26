from flask import Flask, request, jsonify
import pymysql.cursors

app = Flask(__name__)

# MySQL configuration
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'password'
MYSQL_DB_NAME = 'test'

# Establish connection to MySQL database
connection = pymysql.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DB_NAME,
    cursorclass=pymysql.cursors.DictCursor
)

# Vulnerable endpoint
@app.route('/vulnerable/user/<int:user_id>', methods=['GET'])
def vulnerable_user(user_id):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE id = " + str(user_id)
            cursor.execute(sql)
            result = cursor.fetchall()
            return jsonify(result)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)

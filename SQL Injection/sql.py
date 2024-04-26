import sqlite3

def fetch_user(username):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Insecure code: directly concatenating user input into the SQL query
    query = "SELECT * FROM users WHERE username='" + username + "'"
    cursor.execute(query)

    user = cursor.fetchone()

    conn.close()
    return user

# Example usage
username = input("Enter username: ")
user = fetch_user(username)
if user:
    print("User found:", user)
else:
    print("User not found.")

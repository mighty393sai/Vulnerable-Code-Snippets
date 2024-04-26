#include <iostream>
#include <mysql/mysql.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <username>" << std::endl;
        return 1;
    }

    std::string username = argv[1];

    MYSQL *conn;
    MYSQL_RES *res;
    MYSQL_ROW row;

    conn = mysql_init(NULL);
    if (conn == NULL) {
        std::cerr << "Error initializing MySQL connection" << std::endl;
        return 1;
    }

    if (mysql_real_connect(conn, "localhost", "username", "password", "mydatabase", 0, NULL, 0) == NULL) {
        std::cerr << "Error connecting to database: " << mysql_error(conn) << std::endl;
        mysql_close(conn);
        return 1;
    }

    // Insecure code: concatenate user input directly into the SQL query
    std::string query = "SELECT * FROM users WHERE username = '" + username + "'";
    if (mysql_query(conn, query.c_str()) != 0) {
        std::cerr << "Error executing query: " << mysql_error(conn) << std::endl;
        mysql_close(conn);
        return 1;
    }

    res = mysql_store_result(conn);
    if (res == NULL) {
        std::cerr << "Error storing result set: " << mysql_error(conn) << std::endl;
        mysql_close(conn);
        return 1;
    }

    row = mysql_fetch_row(res);
    if (row != NULL) {
        std::cout << "User found: " << row[0] << std::endl;
    } else {
        std::cout << "User not found." << std::endl;
    }

    mysql_free_result(res);
    mysql_close(conn);

    return 0;
}

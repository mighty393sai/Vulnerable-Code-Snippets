package main

import (
    "database/sql"
    "fmt"
    _ "github.com/mattn/go-sqlite3"
    "os"
)

func fetchUser(db *sql.DB, username string) (string, error) {
    var user string

    // Insecure code: directly concatenating user input into SQL query
    query := fmt.Sprintf("SELECT username FROM users WHERE username = '%s'", username)

    // Execute the query
    rows, err := db.Query(query)
    if err != nil {
        return "", err
    }
    defer rows.Close()

    // Process the result
    if rows.Next() {
        err := rows.Scan(&user)
        if err != nil {
            return "", err
        }
    }

    return user, nil
}

func main() {
    // Open the SQLite database
    db, err := sql.Open("sqlite3", "example.db")
    if err != nil {
        fmt.Println("Error opening database:", err)
        os.Exit(1)
    }
    defer db.Close()

    // Example usage
    var username string
    fmt.Print("Enter username: ")
    fmt.Scanln(&username)

    user, err := fetchUser(db, username)
    if err != nil {
        fmt.Println("Error fetching user:", err)
        return
    }

    if user != "" {
        fmt.Println("User found:", user)
    } else {
        fmt.Println("User not found.")
    }
}

#!/bin/bash

# Unsafe script vulnerable to SQL injection
echo "Enter username:"
read username

# Vulnerable SQL query concatenating user input directly
query="SELECT * FROM users WHERE username='$username'"
echo "Executing query: $query"

# Execute the query (this is just an example, not a real execution)
# command_to_execute $query

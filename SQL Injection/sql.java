import java.sql.*;

public class Main {
    public static void main(String[] args) {
        String username = args[0]; // Get username from command line arguments

        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;

        try {
            // Connect to the database
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydatabase", "username", "password");

            // Create a statement
            stmt = conn.createStatement();

            // Insecure code: concatenate user input directly into the SQL query
            String query = "SELECT * FROM users WHERE username = '" + username + "'";

            // Execute the query
            rs = stmt.executeQuery(query);

            // Process the result
            if (rs.next()) {
                System.out.println("User found: " + rs.getString("username"));
            } else {
                System.out.println("User not found.");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // Close resources
            try {
                if (rs != null) rs.close();
                if (stmt != null) stmt.close();
                if (conn != null) conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}

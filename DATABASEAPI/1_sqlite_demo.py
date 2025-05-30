"""
1_sqlite_demo.py
----------------
This script demonstrates how to use Python's built-in sqlite3 module to interact with a SQLite database.

Key Concepts:
1. What is DB-API?
2. Connecting to a database
3. Creating tables, inserting, querying, and updating data
4. Using context managers for database operations

What is DB-API?
---------------
- DB-API is a standard Python interface for database access. Most Python database libraries (including sqlite3) follow this standard.
- sqlite3 is included with Python and requires no external installation.

Scenario:
- Create a simple bank customers table, insert data, and query it.
"""

import sqlite3

# Connect to a database (creates the file if it doesn't exist)
conn = sqlite3.connect('bank.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()



# Delete the table if it exists, then create a new one
cur.execute('DROP TABLE IF EXISTS customers')
cur.execute('''
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    balance REAL NOT NULL
)
''')

# Insert some data (with email)
cur.execute("INSERT INTO customers (name, email, balance) VALUES (?, ?, ?)", ("Alice", "alice@example.com", 1200.0))
cur.execute("INSERT INTO customers (name, email, balance) VALUES (?, ?, ?)", ("Bob", "bob@example.com", 1500.0))
# Function to delete a customer by email, with existence check
def delete_customer_by_email(email):
    cur.execute("SELECT 1 FROM customers WHERE email = ?", (email,))
    if cur.fetchone() is None:
        print(f"Error: No customer found with email {email}")
        return
    cur.execute("DELETE FROM customers WHERE email = ?", (email,))
    conn.commit()
    print(f"Customer with email {email} deleted.")

# Example usage: delete Bob by email
delete_customer_by_email("bob@example.com")
conn.commit()

# Query the data
cur.execute("SELECT * FROM customers")
rows = cur.fetchall()
print("All customers:")
for row in rows:
    print(row)

# Update a balance
cur.execute("UPDATE customers SET balance = balance + 500 WHERE name = ?", ("Alice",))
conn.commit()

# Query again
cur.execute("SELECT * FROM customers WHERE name = ?", ("Alice",))
print("\nAfter updating Alice's balance:")
print(cur.fetchone())

# Clean up
cur.close()
conn.close()

print("""
Explanation:
- This script creates a SQLite database, adds a table, inserts and queries data, and updates a record.
- sqlite3 is a DB-API 2.0 compliant module, so the same code structure works for other databases (with minor changes).
- For other databases (MySQL, PostgreSQL, etc.), you would use a different library but similar code.
""")

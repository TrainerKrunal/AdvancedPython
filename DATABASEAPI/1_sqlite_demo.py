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

# Create a table
cur.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    balance REAL NOT NULL
)
''')

# Insert some data
cur.execute("INSERT INTO customers (name, balance) VALUES (?, ?)", ("Alice", 1200.0))
cur.execute("INSERT INTO customers (name, balance) VALUES (?, ?)", ("Bob", 1500.0))
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

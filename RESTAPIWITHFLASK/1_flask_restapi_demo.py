"""
1_flask_restapi_demo.py
-----------------------
This script demonstrates how to build a simple REST API using Flask in Python.

Key Concepts:
1. What is Flask?
2. Creating RESTful endpoints (GET, POST)
3. Running a Flask app
4. Difference between Flask and Requests library

What is Flask?
--------------
- Flask is a lightweight web framework for Python, ideal for building web applications and REST APIs.
- It is easy to use and requires minimal setup.

What is the Requests library?
-----------------------------
- Requests is a popular Python library for making HTTP requests to other web services or APIs.
- It is used to consume (call) APIs, not to build them.

Difference between Flask and Requests:
-------------------------------------
- **Flask** is used to create web servers and REST APIs. You use Flask when you want to expose your own endpoints (for example, to let others access your data or services over HTTP).
- **Requests** is used to connect to and consume APIs provided by others. You use Requests when you want to fetch data from, or send data to, an external web service or REST API.

Which should you use, and when?
-------------------------------
- Use **Flask** when you are building a web application or REST API server (for example, exposing your bank's customer data to a frontend or other systems).
- Use **Requests** when you are writing a client or script that needs to interact with an existing web API (for example, fetching exchange rates from a public API, or posting data to another service).


How to install Flask:
---------------------
- Using pip (in terminal or command prompt):
    pip install flask
- To check the installed version:
    pip show flask
  or, in Python code:
    import flask; print(flask.__version__)

How to add Flask to IntelliJ IDEA / PyCharm:
--------------------------------------------
1. Open your Python file or project in IntelliJ IDEA or PyCharm.
2. Go to File > Settings > Project: <your_project> > Python Interpreter.
3. Click the '+' icon, search for 'flask', and click 'Install Package'.
4. Flask will be added to your project's environment and available for import.

Scenario:
- Create a simple REST API for managing bank customers (in-memory data, no database).
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store for demo purposes
customers = [
    {"id": 1, "name": "Alice", "balance": 1200.0},
    {"id": 2, "name": "Bob", "balance": 1500.0}
]

@app.route('/customers', methods=['GET'])
def get_customers():
    """Return all customers as JSON."""
    return jsonify(customers)

@app.route('/customers', methods=['POST'])
def add_customer():
    """Add a new customer from JSON data in the request body."""
    data = request.get_json()
    new_id = max(c["id"] for c in customers) + 1 if customers else 1
    new_customer = {"id": new_id, "name": data["name"], "balance": data["balance"]}
    customers.append(new_customer)
    return jsonify(new_customer), 201


# This block ensures the Flask app runs only if this script is executed directly (not imported as a module)
if __name__ == "__main__":
    # app.run(debug=True) starts the Flask development server
    # debug=True enables auto-reload and better error messages during development
    app.run(debug=True)

"""
Further Explanation:
--------------------
1. app = Flask(__name__):
   - This creates a Flask application instance.
   - __name__ is a special variable in Python. Passing it helps Flask know where to look for resources (like templates).
   - This is required to set up the app and register routes.

2. @app.route('/customers', methods=['GET']):
   - This is a decorator that tells Flask to execute the decorated function when a GET request is made to /customers.
   - You can use different routes and HTTP methods (GET, POST, PUT, DELETE) to build a RESTful API.

3. if __name__ == "__main__":
   - This block ensures the Flask app runs only if this script is executed directly (not imported as a module).
   - app.run(debug=True) starts the Flask development server on localhost (127.0.0.1:5000) with debug mode enabled.
   - In production, you would use a production-ready server (not debug mode).
"""

"""
Explanation:
- Run this script and visit http://127.0.0.1:5000/customers in your browser to see all customers (GET).
- Use a tool like Postman or curl to POST new customer data to the same endpoint.
- Flask makes it easy to build and test REST APIs in Python.
"""

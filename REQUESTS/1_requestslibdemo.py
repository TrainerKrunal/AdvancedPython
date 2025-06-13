"""
1_requestslibdemo.py
---------------------
This script demonstrates how to use the 'requests' library in Python to make HTTP requests.

# How to install the requests library:
# ------------------------------------
# Using pip (in terminal or command prompt):
#     pip install requests
# In PyCharm/IntelliJ IDEA:
#     1. Open the Python file or project.
#     2. Go to File > Settings > Project: <your_project> > Python Interpreter.
#     3. Click the '+' icon, search for 'requests', and click 'Install Package'.

Key Concepts:
1. What is the requests library?
2. How to make GET and POST requests
3. How to handle responses and errors

What is the requests library?
----------------------------
- 'requests' is a popular third-party Python library for making HTTP requests easily.
- It simplifies sending HTTP/1.1 requests, handling responses, and working with APIs.

Scenario:
- Fetching data from a public API (JSONPlaceholder) using GET
- Sending data to the API using POST
"""

import requests

# Example 1: Making a GET request
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

if response.status_code == 200:
    data = response.json()  # Parse JSON response
    print("GET request successful. Post data:")
    print(data)
else:
    print(f"GET request failed with status code: {response.status_code}")

# Example 2: Making a POST request
payload = {
    'title': 'Advanced Python',
    'body': 'This is a test post created during training.',
    'userId': 1
}

post_response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)

if post_response.status_code == 201:
    print("\nPOST request successful. Created post:")
    print(post_response.json())
else:
    print(f"POST request failed with status code: {post_response.status_code}")

print("""
Explanation:
- The GET request fetches a post from a fake online REST API and prints the result.
- The POST request sends new data to the API and prints the created resource.
- The requests library makes it easy to work with web APIs in Python.
""")

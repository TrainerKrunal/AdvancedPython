"""
1_jinjatemplateDemo.py
----------------------
This script demonstrates the basics of Jinja2 templating in Python.

# How to install Jinja2:
# ----------------------
# Using pip (in terminal or command prompt):
#     pip install jinja2
#     pip show jinja2 : to show the installed version
# In PyCharm/IntelliJ IDEA:
#     1. Open the Python file or project.
#     2. Go to File > Settings > Project: <your_project> > Python Interpreter.
#     3. Click the '+' icon, search for 'jinja2', and click 'Install Package'.

Key Concepts:
1. What is Jinja2?
2. Why do we need templates?
3. How to use Jinja2 to render templates

What is Jinja and Jinja2?
-------------------------
- **Jinja** is a modern and designer-friendly templating language for Python, inspired by Django’s templates. It allows you to create text-based formats (like HTML, XML, emails, or configuration files) by combining static content with dynamic data.
- **Jinja2** is the second major version of Jinja, and is the most widely used version. It is a standalone package and is the default templating engine for the Flask web framework.
- Jinja2 provides a powerful, flexible, and secure way to generate dynamic content, supporting variables, loops, conditionals, template inheritance, filters, and more.

Why is Jinja2 useful?
---------------------
- **Separation of Concerns:** Jinja2 helps keep your business logic (Python code) separate from your presentation layer (HTML or other text files). This makes your codebase cleaner and easier to maintain.
- **Dynamic Content:** You can generate dynamic web pages or documents by injecting data into templates at runtime (e.g., displaying user account balances, transaction histories, or personalized messages in a banking app).
- **Reusability:** Templates can be reused and extended, reducing duplication and making it easier to update the look and feel of your application.
- **Security:** Jinja2 automatically escapes variables by default, helping to prevent common web vulnerabilities like Cross-Site Scripting (XSS).

What is Jinja2?
---------------
- Jinja2 is a powerful templating engine for Python, used to generate dynamic text files (like HTML, XML, or even plain text).
- It is commonly used with web frameworks like Flask to separate business logic from presentation (HTML).

Why do we need templates?
-------------------------
- Templates allow you to generate dynamic content by combining static structure (like HTML) with dynamic data (variables, loops, conditions).
- This keeps your code clean and maintainable, separating logic from layout.

Example:
- Render a simple HTML template with dynamic data using Jinja2.
"""

from jinja2 import Template

# Define a template string (could also be loaded from a file)
template_str = """
<html>
  <head><title>Bank Customers</title></head>
  <body>
    <h1>Customer List</h1>
    <ul>
    {% for customer in customers %}
      <li>{{ customer.name }} (Balance: {{ customer.balance }})</li>
    {% endfor %}
    </ul>
  </body>
</html>
"""

# Data to render in the template
customers = [
    {"name": "Alice", "balance": 1200.0},
    {"name": "Bob", "balance": 1500.0},
    {"name": "Charlie", "balance": 2000.0}
]

# Create a Template object
jinja_template = Template(template_str)

# Render the template with data
rendered_html = jinja_template.render(customers=customers)

print(rendered_html)

print("""
Explanation:
- The template uses {{ ... }} for variables and {% ... %} for control structures (loops, if statements).
- jinja_template.render(customers=customers) fills the template with data.
- Jinja2 is widely used in web development for generating dynamic HTML pages.
""")

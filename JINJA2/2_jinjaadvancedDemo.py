"""
2_jinjaadvancedDemo.py
----------------------
This script demonstrates advanced Jinja2 template features, including template inheritance, filters, and conditionals.

Scenario:
- Render a bank statement for a customer, showing transactions and using template inheritance for layout.
"""

from jinja2 import Environment, FileSystemLoader
import os

current_dir = os.path.dirname(__file__)
env = Environment(loader = FileSystemLoader(current_dir))

base_template = """
<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
        <h1>{{ title }}</h1>
         
        {% block content %}{% endblock %}
    </body>
</html>
        
"""

with open(os.path.join(current_dir,"layout.html"),"w",encoding="utf-8") as f:
    f.write(base_template)

customer={"name": "Alice", "balance": 1000}
transactions=[
    {"date": "2023-01-01", "amount": 100, "type": "deposit"},
    {"date": "2023-01-02", "amount": 50, "type": "withdrawal"},
    {"date": "2023-01-03", "amount": 200, "type": "deposit"}
]

title="Bank Customers with Jinja2"

template = env.get_template("advance.html")
rendered_html = template.render(customer=customer,title=title,transactions=transactions)

output_path= os.path.join(current_dir, "output.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(rendered_html)

print("Rendered HTML has been saved to rendered.html. Open this file in your browser to view the result.")

print("""
Explanation:
- layout.html is a base template with a block for content.
- advance.html extends layout.html and fills in the content block.
- The template uses filters (capitalize), loops, and conditionals.
- This approach is common in web apps for consistent layouts and dynamic content.
""")

"""
2_jinjaadvancedDemo.py
----------------------
This script demonstrates advanced Jinja2 template features, including template inheritance, filters, and conditionals.

Scenario:
- Render a bank statement for a customer, showing transactions and using template inheritance for layout.
"""

from jinja2 import Environment, FileSystemLoader
import os

# Set up Jinja2 environment to load templates from the current directory
current_dir = os.path.dirname(__file__)
env = Environment(loader=FileSystemLoader(current_dir))

# Create base template (layout.html)
base_template = '''
<html>
  <head><title>{{ title }}</title></head>
  <body>
    <h1>{{ title }}</h1>
    {% block content %}{% endblock %}
  </body>
</html>
'''


# Save base template to file (layout.html) if not already present
with open(os.path.join(current_dir, 'layout.html'), 'w', encoding='utf-8') as f:
    f.write(base_template)

# Data for rendering
customer = {"name": "Alice", "balance": 3200.0}
transactions = [
    {"date": "2025-05-01", "type": "deposit", "amount": 2000},
    {"date": "2025-05-03", "type": "withdrawal", "amount": 500},
    {"date": "2025-05-10", "type": "deposit", "amount": 1700},
]


# Now use advance.html as the template
template = env.get_template('advance.html')
rendered_html = template.render(title="Bank Statement", customer=customer, transactions=transactions)

# Save the rendered HTML to a file for easy viewing in a browser
output_path = os.path.join(current_dir, 'rendered.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(rendered_html)

print("Rendered HTML has been saved to rendered.html. Open this file in your browser to view the result.")

print("""
Explanation:
- layout.html is a base template with a block for content.
- advance.html extends layout.html and fills in the content block.
- The template uses filters (capitalize), loops, and conditionals.
- This approach is common in web apps for consistent layouts and dynamic content.
""")

"""
1_beautifulsoup.py
-------------------
This script demonstrates how to use the BeautifulSoup library in Python for web scraping and HTML parsing.

Key Concepts:
1. What is BeautifulSoup?
2. How to parse HTML and extract data
3. Basic usage example

What is BeautifulSoup?
----------------------
- BeautifulSoup is a popular Python library for parsing HTML and XML documents.
- It is commonly used for web scraping, i.e., extracting data from web pages.

How to install BeautifulSoup:
-----------------------------
- Using pip:
      pip install beautifulsoup4
- In PyCharm/IntelliJ IDEA:
      1. Open the Python file or project.
      2. Go to File > Settings > Project: <your_project> > Python Interpreter.
      3. Click the '+' icon, search for 'beautifulsoup4', and click 'Install Package'.

Example:
- Parse a simple HTML document and extract data from it.
"""


import os
from bs4 import BeautifulSoup

# Read HTML content from an external file (home.html) in the same directory as this script
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'home.html')
with open(file_path, 'r', encoding='utf-8') as file:
    html_doc = file.read()

# Parse the HTML document
soup = BeautifulSoup(html_doc, 'html.parser')

# Extract the title
title = soup.title.string
print(f"Page Title: {title}")

# Extract all branch names
branches = soup.find_all('li', class_='branch')
print("Branches:")
for branch in branches:
    print(f"- {branch.text}")

# Extract the contact email
contact = soup.find('p').text
print(f"Contact Info: {contact}")

print("""
Explanation:
- BeautifulSoup parses the HTML and allows you to search and extract elements easily.
- soup.title.string gets the content of the <title> tag.
- soup.find_all('li', class_='branch') finds all <li> elements with class 'branch'.
- soup.find('p').text gets the text of the first <p> tag.
- This is a basic example; BeautifulSoup can handle much more complex HTML structures.
""")

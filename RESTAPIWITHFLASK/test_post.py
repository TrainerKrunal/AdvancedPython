import requests

url = "http://127.0.0.1:5000/customers"
data = {"name": "Bob", "balance": 1000}
response = requests.post(url, json=data)
print(response.status_code, response.json())
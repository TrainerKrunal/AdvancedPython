import json

data={
    "name":"Krunal",
    "age":40,
    "skills":["Python","Azure","DevOps"],
    "isSalaried":True
}

json_string=json.dumps(data,indent=4)
print(json_string)


with open("data.json","w") as json_file:
    json.dump(data,json_file,indent=4)
print("JSON data is written to the file.")

with open("data.json","r") as json_read_file:
    mydata = json.load(json_read_file) #reads data from file

print("Name:", mydata["name"])
print("Services:",mydata["skills"])

json_string='[{"name":"Krunal","age":37},{"name":"Aaditya","age":12}]'
people = json.loads(json_string)

for person in people:
    print(f"{person["name"]} is {person["age"]} years old!")

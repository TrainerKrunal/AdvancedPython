import xml.etree.ElementTree as ET

# Create root element
root = ET.Element("employees")

# Create employee node
employee = ET.SubElement(root, "employee")

# Add attribute
employee.set("id", "E101")

# Create child elements
name = ET.SubElement(employee, "name")
name.text = "Krunal"

department = ET.SubElement(employee, "department")
department.text = "AI"

city = ET.SubElement(employee, "city")
city.text = "Ahmedabad"

# Create tree
tree = ET.ElementTree(root)

# Save XML file
tree.write("XMLDemo/employees.xml")

print("XML File Created Successfully")

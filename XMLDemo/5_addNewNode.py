import xml.etree.ElementTree as ET

tree = ET.parse('XMLDemo/students.xml')

root = tree.getroot()

# Create new student
new_student = ET.SubElement(root, 'student')

# Add attribute
new_student.set('id', '103')

# Add child elements
name = ET.SubElement(new_student, 'name')
name.text = 'Aditya'

course = ET.SubElement(new_student, 'course')
course.text = 'React'

city = ET.SubElement(new_student, 'city')
city.text = 'Pune'

# Save updated XML
tree.write('XMLDemo/new_students.xml')

print("New Student Added Successfully")

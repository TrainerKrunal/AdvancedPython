import xml.etree.ElementTree as ET

tree = ET.parse('XMLDemo/students.xml')

root = tree.getroot()

first_student = root.find('student')

print(first_student.find('name').text)
print(first_student.find('course').text)

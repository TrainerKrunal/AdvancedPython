import xml.etree.ElementTree as ET

# Load XML file
tree = ET.parse('XMLDemo/students.xml')

# Get root element
root = tree.getroot()

print("Root Tag :", root.tag)

print("\n===== STUDENT DETAILS =====\n")

# Read all students
for student in root.findall('student'):

    student_id = student.get('id')

    name = student.find('name').text
    course = student.find('course').text
    city = student.find('city').text

    print("ID :", student_id)
    print("Name :", name)
    print("Course :", course)
    print("City :", city)

    print("------------------------")

import xml.etree.ElementTree as ET

tree = ET.parse('XMLDemo/students.xml')

root = tree.getroot()

# Update course name
for student in root.findall('student'):

    if student.get('id') == '101':

        student.find('course').text = "Generative AI"

# Save updated file
tree.write('XMLDemo/updated_students.xml')

print("XML Updated Successfully")

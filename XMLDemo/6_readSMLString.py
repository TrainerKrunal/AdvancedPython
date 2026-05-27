import xml.etree.ElementTree as ET

xml_data = '''

<book>

    <title>Python Masterclass</title>

    <author>Krunal</author>

</book>

'''

root = ET.fromstring(xml_data)

print("Title :", root.find('title').text)
print("Author :", root.find('author').text)

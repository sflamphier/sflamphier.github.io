import json
import xml.etree.ElementTree as ET

# Load the JSON file
with open('restaurants.json') as json_file:
    data = json.load(json_file)

# Create the root element for XML
root = ET.Element("restaurants")

# Loop through the restaurants and add to the XML
for restaurant in data['restaurants']:
    restaurant_element = ET.SubElement(root, "restaurant")
    
    for key, value in restaurant.items():
        child = ET.SubElement(restaurant_element, key)
        child.text = str(value)

# Create a tree object and save it as XML
tree = ET.ElementTree(root)
tree.write('restaurants.xml')

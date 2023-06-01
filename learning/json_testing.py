import json

# Convert Python dict to JSON object

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# The sort_keys method will sort the Python dict into an alphabetical JSON object. The 's' in dump(s) means 'str'.
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)


# Output JSON data within a file:
"""
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

# Read JSON data within JSON file:
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)
"""
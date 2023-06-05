import json

# Convert Python dict to JSON object

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# The sort_keys method will sort the Python dict into an alphabetical JSON object. The 's' in dump(s) means 'str'.
personJSON = json.dumps(person, indent=4, sort_keys=True)
print('This is an example of converting a Python dict to JSON object' + str(personJSON))

# Output JSON data within a file:
"""
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

# Read JSON data within JSON file:
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)
"""

# Encode custom objects

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable.')
    
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)
userJSON = UserEncoder().encode(user)
print('\nThis is an example of endoding a custom object' + str(userJSON))

# Decode custom objects

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)
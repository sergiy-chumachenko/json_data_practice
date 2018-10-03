# JavaScript Object Notation
# JSON Dumps and Loads

import json
from pprint import pprint

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmish@gmail.com", "john.smith@yahoo.com"],
            "has_licence": false
        },
        {
            "name": "Albert Potter",
            "phone": "615-555-3213",
            "emails": ["albert.potter@gmail.com", "albertpotter@yahoo.com"],
            "has_licence": true
        }
    ]
}
'''
# Transform JSON string into Python Object (dict)
data = json.loads(people_string)
pprint(data)
pprint(type(data))
pprint(type(data['people']))
for person in data['people']:
    pprint(person)
    pprint("*"*25)
    pprint(person['name'])

# Transform Dict Python Object into JSON string
for person in data['people']:
    del person["phone"]
pprint(data)
# indent for space
# sort_keys = True --> Sorting keys
new_people_string = json.dumps(data, indent=2, sort_keys=True)
print(new_people_string)
pprint(type(new_people_string))
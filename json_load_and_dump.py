# JavaScript Object Notation
# Using load method to load the JSON file into Python Object

import json
from pprint import pprint

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    pprint(state['name'])
    pprint(state['abbreviation'])
    del state["area_codes"]
pprint(data['states'])

# Using dump method to write Python Object Dict into JSON file
# Indent adding spaces for make more readable representation

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)

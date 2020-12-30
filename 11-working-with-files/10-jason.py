import json
from pprint import pprint

policy = None

with open('file.json', 'r') as service_file:
  policy =json.load(service_file)
  pprint(policy)

  policy['Statement']['Effect'] = 'Denied'
  pprint(policy)

  with open('file1.json', 'w') as service_file:
    json.dump(policy, service_file)

with open('file1.json', 'r') as service_file:
  pprint(json.load(service_file))

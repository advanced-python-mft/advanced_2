import json

d = {'apple':'sib', 2:6, 7:[2, 4, 5, 65]}

with open('file.json', 'w') as f:
    json.dump(d, f)

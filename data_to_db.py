import json

with open('data.py', 'r') as f:
    data = f.read()

with open('db.json', 'w') as db:
    json.dump(data, db)

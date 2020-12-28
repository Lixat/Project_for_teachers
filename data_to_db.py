import json

with open('data.py', 'r') as f:
    data = f.read()

with open('db.json', 'w', encoding='utf-8') as db:
    json.dump(data, db)

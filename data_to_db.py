import json

from data import goals, teachers

data = {}
data['goals'] = goals
data['teachers'] = teachers

with open('db.json', 'w', encoding='utf-8') as db:
    json.dump(data, db)

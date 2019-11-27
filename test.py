import json

with open('json/calendario20191126-211532.json', encoding='utf-8') as file:
      data = json.load(file)

array = []
for record in data:
      print(record)
      
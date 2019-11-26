import json
data = []

name = 'calendario20191125-221000.json'

with open(f'json/{name}') as file:
    data = json.load(file)

print(data)
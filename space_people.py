import requests

people = requests.get('http://api.open-notify.org/astros.json')
json = people.json()
print('Student emails')

for people in json['people']:
    print(people['name'])
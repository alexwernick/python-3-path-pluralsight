import requests

people = requests.get('http://api.open-notify.org/astros.json')
json = people.json()

print('Names:')
for people in json['people']:
    print(people['name'])
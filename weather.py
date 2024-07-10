import requests

city = 'London'

response = requests.get('http://api.weatherapi.com/v1/current.json?key=3bd3c330632d499084a74622241007&q=' + city + '&aqi=no')
json = response.json()

temperature = json.get('current').get('temp_f')
description = json.get('current').get('condition').get('text')

print("Today's weather in", city ,"is", description, 'and', temperature, 'degrees')

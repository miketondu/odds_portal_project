import requests

url = 'http://localhost:12345/results'
r = requests.post(url,json={'home_team':20, 'away_team':20, 'altitude':1})

print(r.json())

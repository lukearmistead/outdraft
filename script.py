import pandas as pd
from pprint import pprint
import json
import requests
import yaml

# https://curlconverter.com/
# https://api.fantasypros.com/public/v2/docs/
with open("creds.yml", 'r') as stream:
    creds = yaml.safe_load(stream)
season = '2017'
position = 'QB'
week = 0
headers = creds

params = {
    'position': ['QB', 'RB'],
    'week': '0',
    'scoring': 'HALF',
    'type': 'ROS', # Rest of season
    }
url = f'https://api.fantasypros.com/public/v2/json/nfl/{season}/consensus-rankings'
response = requests.get(url, headers=headers, params=params)

payload = response.json()
pprint(payload)
pprint(type(payload))
# df = pd.DataFrame(payload)
# pprint(df.season.unique())

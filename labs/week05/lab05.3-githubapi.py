import requests
import json
from config import config

apikey = config['github_api']

url = 'https://api.github.com/repos/tomdbrophy/privaterepo'

response = requests.get(url, auth = ('token', apikey))

print(response.status_code)

repo_json = response.json()

with open ('privaterepo.txt', 'w') as fp:
    json.dump(repo_json, fp, indent=4)
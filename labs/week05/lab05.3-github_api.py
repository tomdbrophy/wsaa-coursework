import requests
import urllib.parse
from config import config as cfg
import json

#url = 'https://github.com/tomdbrophy/wsaa-coursework'
url = 'https://github.com/tomdbrophy/aprivateone'

api_key = cfg['api_key']
response = requests.get(url, auth=('token', api_key))

print(response.status_code)
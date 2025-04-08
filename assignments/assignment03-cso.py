import requests
import json

# URL for the dataset
url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en'

# Fetch the data from the URL
with open ('exchequer_data.json', 'wt') as fp:
    response = requests.get(url)
    print(json.dumps(response.json()), file=fp)
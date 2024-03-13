import requests
import urllib.parse

target_url = 'https://www.wikipedia.org/'

api_key = ''

api_url = 'https://api.html2pdf.app/v1/generate'
'''
params = {'url':target_url, 'api_key':api_key}
parsed_params = urllib.parse.urlencode(params)
request_url = api_url+'?'+parsed_params
'''

request_url = ''

response = requests.get(request_url)
print(response.status_code)

result = response.content
with open('document.pdf', 'wb') as handler:
    handler.write(result) 
from github import Github
import requests
from config import config as cfg

# Link to key in config file
apikey = cfg['githubkey']

# Creat Github instance
g = Github(apikey)

# Link to specific repo being used
repo = g.get_repo('tomdbrophy/assignment04')
#print(repo.clone_url)

# Retrieve info for file in Github repository
file_info = repo.get_contents('text.txt')
file_url = file_info.download_url
#print(file_url)

# Retrieve text from file in Github repository
response = requests.get(file_url)
contents = response.text
#print(contents)

# Amend contents of the file to replace Andrew with Tom
amended_contents = contents.replace('Andrew', 'Tom')

# Write the amended contents to a new file
with open ('andrewtotom.txt', 'w') as fp:
    fp.write(amended_contents)

# Update Github with the amended text
github_response = repo.update_file(file_info.path, 'automated replacement of text', amended_contents, file_info.sha)

print(github_response)
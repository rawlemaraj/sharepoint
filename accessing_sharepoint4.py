import requests
from requests_ntlm import HttpNtlmAuth

# Your SharePoint URL, library and file
sharepoint_url = 'http://sharepoint_url'
document_library = 'DocumentLibrary'
file_name = 'filename.txt'

# Create the URL for the file
file_url = f'{sharepoint_url}/{document_library}/{file_name}'

# Your credentials
username = 'domain\\username'
password = 'password'

# Create a session and authenticate
session = requests.Session()
session.auth = HttpNtlmAuth(username, password)

# Get the file
response = session.get(file_url, stream=True)

# Write the file
with open(file_name, 'wb') as out_file:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            out_file.write(chunk)

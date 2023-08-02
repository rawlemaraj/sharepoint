import os
from requests import Session
from requests_ntlm import HttpNtlmAuth

# SharePoint site and file details
sharepoint_url = 'https://sharepoint-site.com'
site_url = 'sites/MySite'
folder_path = '/Shared Documents/MyFolder'
local_file_path = '/path/to/your/local/file.txt'
remote_file_name = 'file.txt'

# Credentials
username = 'domain\\username'
password = 'password'

# URL to the folder where you want to upload the file
upload_url = f"{sharepoint_url}/{site_url}/_api/web/GetFolderByServerRelativeUrl('{folder_path}')/Files/add(url='{remote_file_name}',overwrite=true)"

# Read the file data
with open(local_file_path, 'rb') as file_data:
    file_contents = file_data.read()

# Create a session and authenticate
session = Session()
session.auth = HttpNtlmAuth(username, password)

# Set headers and make the POST request
headers = {'Content-Type': 'application/octet-stream'}
response = session.post(upload_url, headers=headers, data=file_contents, verify=False)

# Check the result
if response.status_code == 200:
    print('File uploaded successfully.')
else:
    print('Failed to upload file.')
    print('Status code:', response.status_code)
    print('Response:', response.text)

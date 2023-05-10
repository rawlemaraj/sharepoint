import requests
from requests_ntlm import HttpNtlmAuth
from getpass import getpass

sharepoint_url = 'http://sharepoint-site/path/to/your/file.docx'
username = 'domain\\username'
password = getpass('Enter your password: ')

response = requests.get(sharepoint_url, auth=HttpNtlmAuth(username, password), stream=True)

if response.status_code == 200:
    with open('filename.docx', 'wb') as file:
        for chunk in response.iter_content(chunk_size=128):
            file.write(chunk)
    print('File downloaded successfully.')
else:
    print('Failed to download file. Status code:', response.status_code)

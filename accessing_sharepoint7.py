import requests
from requests_ntlm import HttpNtlmAuth

sharepoint_url = 'https://yoursharepoint.com/path/to/your/file.txt'
username = 'DOMAIN\\username'
password = 'password'

response = requests.get(sharepoint_url, auth=HttpNtlmAuth(username, password), verify=False)

# check for successful GET request
if response.status_code == 200:
    with open('downloaded_file.txt', 'wb') as f:
        f.write(response.content)
else:
    print(f'Failed to download file. Status code: {response.status_code}')

import requests
from requests_ntlm import HttpNtlmAuth

sharepoint_site = 'your_sharepoint_site'
username = 'your_username'
password = 'your_password'
file_to_delete = 'file_to_delete'  # this should be a relative path to your file

session = requests.Session()
session.auth = HttpNtlmAuth(username, password)

delete_url = f"{sharepoint_site}/_api/web/GetFileByServerRelativeUrl('{file_to_delete}')"

headers = {
    'IF-MATCH': '*',
    'X-HTTP-Method': 'DELETE',
}

response = session.post(delete_url, headers=headers)

if response.status_code == 200:
    print(f"File '{file_to_delete}' was deleted successfully.")
else:
    print(f"Failed to delete the file. Status code: {response.status_code}")

import requests
from requests.auth import HTTPBasicAuth
import json

url = 'https://[your-sharepoint-site-url]'
client_id = '[client-id]'
client_secret = '[client-secret]'
path_to_file = '[path-to-your-file]'

# First, get the FormDigestValue
digest_url = url + "/_api/contextinfo"
headers = {
    'accept': "application/json;odata=verbose"
    }
response = requests.post(digest_url, headers=headers, auth=HTTPBasicAuth(client_id, client_secret))
digest_value = response.json()['d']['GetContextWebInformation']['FormDigestValue']

# Now, use the digest value to delete the file
delete_url = url + f"/_api/web/GetFileByServerRelativeUrl('{path_to_file}')"
headers = {
    'accept': "application/json;odata=verbose",
    'X-RequestDigest': digest_value,
    'If-Match': "*"
    }
response = requests.post(delete_url, headers=headers, auth=HTTPBasicAuth(client_id, client_secret))

# If the response status code is 200, the file has been deleted successfully
if response.status_code == 200:
    print(f"File at {path_to_file} deleted successfully!")
else:
    print(f"Failed to delete file at {path_to_file}. Response code: {response.status_code}")

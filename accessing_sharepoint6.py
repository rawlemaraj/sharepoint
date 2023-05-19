from shareplum import Site
from shareplum import Office365
from shareplum.site import Version
from requests_ntlm import HttpNtlmAuth
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# setup parameters
username = 'username'  # username for SharePoint
password = 'password'  # password for SharePoint
site_url = 'https://sharepoint-site-url'  # SharePoint Site URL
file_url = 'path-to-file-in-sharepoint'  # URL to the file you want to download
local_file_path = 'path-to-local-file'  # Local path where file needs to be saved

# Setup session with NTLM Authentication
session = requests.Session()
session.auth = HttpNtlmAuth(username, password)

# Setup Shareplum site
authcookie = Office365(site_url, username=username, password=password).GetCookies()
site = Site(site_url, version=Version.v2019, authcookie=authcookie)

# Open the SharePoint file
response = session.get(file_url, stream=True, verify=False)

# Save the file locally
with open(local_file_path, 'wb') as out_file:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            out_file.write(chunk)

print(f"File downloaded to {local_file_path}")

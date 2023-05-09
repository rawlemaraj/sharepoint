# pip install shareplum

from shareplum import Site
from shareplum import Office365
from shareplum.site import Version
import os

# SharePoint site and target file details
username = 'username'
password = 'password'
site_url = 'https://yoursharepointsite.com/sites/your-site-name'
folder_path = 'Shared Documents/Your Folder'
file_name = 'yourfile.ext'  # replace with your file name

# Get session
authcookie = Office365(site_url, username=username, password=password).GetCookies()
site = Site(site_url, version=Version.v2016, authcookie=authcookie)

# Access the folder
folder = site.Folder(folder_path)

# Download file
with open(file_name, 'wb') as f:
    file_content = folder.get_file(file_name)
    f.write(file_content)

print(f'{file_name} downloaded successfully.')

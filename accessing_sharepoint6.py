from shareplum import Site
from shareplum import Office365
from shareplum.site import Version

# setup parameters
username = 'username'  # username for SharePoint
password = 'password'  # password for SharePoint
site_url = 'https://sharepoint-site-url'  # SharePoint Site URL
folder_path = 'path-to-folder-in-sharepoint'  # Path to the folder containing your file
file_name = 'file-name'  # The name of the file you want to download
local_file_path = 'path-to-local-file'  # Local path where file needs to be saved

# authenticate and setup connection to SharePoint
authcookie = Office365(site_url, username=username, password=password).GetCookies()
site = Site(site_url, version=Version.v2019, authcookie=authcookie)

# get SharePoint folder
sp_folder = site.Folder(folder_path)

# download the file
file_content = sp_folder.get_file(file_name)

# save the file locally
with open(local_file_path, 'wb') as out_file:
    out_file.write(file_content)

print(f"File downloaded to {local_file_path}")

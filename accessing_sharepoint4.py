from shareplum import Site
from shareplum import Office365
from shareplum.site import Version

# Set your SharePoint and file details
sharepoint_url = 'https://sharepoint2019site.com'
site_url = 'https://sharepoint2019site.com/sites/my-site'
folder_path = '/Shared Documents/my-folder'
file_name = 'my-file.xlsx'
destination_folder = '/path/to/save/file'

# Set your SharePoint username and password
username = 'username'
password = 'password'

# Set the SharePoint site version
version = Version.v2019

# Authenticate with SharePoint
authcookie = Office365(sharepoint_url, username=username, password=password).GetCookies()
site = Site(site_url, version=version, authcookie=authcookie)

# Get the folder
folder = site.Folder(folder_path)

# Download the file
file_content = folder.get_file(file_name)

# Save the file to the specified folder
local_file_path = os.path.join(destination_folder, file_name)
with open(local_file_path, 'wb') as f:
    f.write(file_content)

print(f'File downloaded successfully and saved to {local_file_path}')

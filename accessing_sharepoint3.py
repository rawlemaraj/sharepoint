import os
import requests
from requests_ntlm import HttpNtlmAuth

# Set your SharePoint and file details
sharepoint_url = 'https://sharepoint2019site.com'
file_relative_path = '/path/to/your/file.txt'
destination_folder = '/path/to/save/file'

# Set your SharePoint username and password
username = 'username'
password = 'password'

# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Create the authentication object
auth = HttpNtlmAuth(f'{username}', f'{password}')

# Download the file
file_url = f'{sharepoint_url}{file_relative_path}'
response = requests.get(file_url, auth=auth)

# Check if the request was successful
if response.status_code == 200:
    # Save the file to the specified folder
    local_file_path = os.path.join(destination_folder, os.path.basename(file_relative_path))
    with open(local_file_path, 'wb') as f:
        f.write(response.content)

    print(f'File downloaded successfully and saved to {local_file_path}')
else:
    print(f'Error downloading file: {response.status_code} - {response.text}')

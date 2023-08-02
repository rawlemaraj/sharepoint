import os
from requests import Session
from requests_ntlm import HttpNtlmAuth

# SharePoint site and file details
sharepoint_url = 'https://sharepoint-site.com'
site_url = 'sites/MySite'
folder_path = 'Shared Documents/MyFolder'
local_file_path = '/path/to/your/local/file.txt'
remote_file_name = 'file.txt'

# Credentials
username = 'domain\\username'
password = 'password'

try:
    # Create a session and authenticate
    session = Session()
    session.auth = HttpNtlmAuth(username, password)

    # Fetch form digest value
    contextinfo_url = f"{sharepoint_url}/{site_url}/_api/contextinfo"
    contextinfo_response = session.post(contextinfo_url, headers={'Accept': 'application/json;odata=verbose'}, verify=False)
    contextinfo = contextinfo_response.json()
    form_digest_value = contextinfo['d']['GetContextWebInformation']['FormDigestValue']

    # URL to the folder where you want to upload the file
    upload_url = f"{sharepoint_url}/{site_url}/_api/web/GetFolderByServerRelativeUrl('{folder_path}')/Files/add(url='{remote_file_name}',overwrite=true)"

    # Read the file data
    with open(local_file_path, 'rb') as file_data:
        file_contents = file_data.read()

    # Set headers and make the POST request
    headers = {
        'Content-Type': 'application/octet-stream',
        'Accept': 'application/json;odata=verbose',
        'X-RequestDigest': form_digest_value,
    }
    response = session.post(upload_url, headers=headers, data=file_contents, verify=False)

    # Check the result
    if response.status_code == 200:
        print('File uploaded successfully.')

        # Parse the response to get the server-relative URL of the uploaded file
        response_json = response.json()
        file_server_relative_url = response_json['d']['ServerRelativeUrl']

        # URL to check in the uploaded file
        checkin_url = f"{sharepoint_url}/{site_url}/_api/web/GetFileByServerRelativeUrl('{file_server_relative_url}')/CheckIn(comment='Checked in by script', checkintype=0)"

        # Make the POST request to check in the file
        response = session.post(checkin_url, headers={'Accept': 'application/json;odata=verbose', 'X-RequestDigest': form_digest_value}, verify=False)

        print('Check-in status code:', response.status_code)
        print('Check-in response:', response.text)
        
        if response.status_code == 204:
            print('File checked in successfully.')
        else:
            print('Failed to check in file.')
    else:
        print('Failed to upload file.')
        print('Status code:', response.status_code)
        print('Response:', response.text)
except Exception as e:
    print('An error occurred:', str(e))

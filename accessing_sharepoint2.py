from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File

url = 'https://yoursite.sharepoint.com/'
username = 'username'
password = 'password'
relative_url = '/Shared Documents/filename.docx'

context_auth = AuthenticationContext(url)
if context_auth.acquire_token_for_user(username, password):
    client_context = ClientContext(url, context_auth)
    web = client_context.web
    client_context.load(web)
    client_context.execute_query()
    print(f'Connected to {web.properties["Url"]}')

    download_path = "./filename.docx"
    with open(download_path, "wb") as local_file:
        File.open_binary(client_context, relative_url, local_file)

    print(f"File downloaded to {download_path}")
else:
    print(context_auth.get_last_error())

from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File

site_url = "http://your_site_url"
ctx_auth = AuthenticationContext(site_url)
username = "your_username"
password = "your_password"

if ctx_auth.acquire_token_for_user(username, password):
    ctx = ClientContext(site_url, ctx_auth)
    relative_url_to_file = "/Shared Documents/myfile.docx"
    file_to_checkout = File.get_file_by_server_relative_url(ctx, relative_url_to_file)
    file_to_checkout.check_out()
    ctx.execute_query()
    print(f"File '{file_to_checkout.properties['Name']}' has been checked out")
else:
    print(ctx_auth.get_last_error())

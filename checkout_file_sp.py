from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext

site_url = "http://your_site_url"
ctx_auth = AuthenticationContext(site_url)
username = "your_username"
password = "your_password"

if ctx_auth.acquire_token_for_user(username, password):
    ctx = ClientContext(site_url, ctx_auth)
    relative_url_to_file = "/Shared Documents/myfile.docx"
    
    file = ctx.web.get_file_by_server_relative_url(relative_url_to_file)
    file.check_out()
    ctx.execute_query()
    
    print(f"File '{relative_url_to_file}' has been checked out")
else:
    print(ctx_auth.get_last_error())

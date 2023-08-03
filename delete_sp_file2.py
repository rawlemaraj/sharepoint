from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File

site_url = "<sharepoint_site_url>"
ctx_auth = AuthenticationContext(url=site_url)
username = "<username>"
password = "<password>"

if ctx_auth.acquire_token_for_user(username, password):
    ctx = ClientContext(site_url, ctx_auth)
    web = ctx.web
    ctx.load(web)
    ctx.execute_query()

    relative_url = "/Shared Documents/myfile.txt"
    file = web.get_file_by_server_relative_url(relative_url)
    file.delete_object()
    ctx.execute_query()

    print("File has been deleted")
else:
    print(ctx_auth.get_last_error())

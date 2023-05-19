This script performs the following tasks:

Setup a session with NTLM Authentication
Setup a connection to the SharePoint site
Open the SharePoint file
Save the file locally
Please replace the placeholder strings (like 'username', 'password', 'https://sharepoint-site-url', 'path-to-file-in-sharepoint', 'path-to-local-file') with your actual values.

Remember that SharePoint URLs can be a bit tricky: the file URL must be the absolute URL to the file in SharePoint, and the site URL must be the URL to your SharePoint site, which is typically the root of your SharePoint site or a specific sub-site URL.

Also, please be aware that the usage of requests_ntlm might be discouraged as it supports NTLMv1 and NTLMv2 which are considered insecure protocols. The preferred way would be to use modern authentication standards.
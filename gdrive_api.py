from pydrive.auth import GoogleAuth

FILE_ID=''

gauth = GoogleAuth()
#gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
# Try to load saved client credentials
gauth.LoadCredentialsFile("client_secrets.json")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("client_secrets.json")


from pydrive.drive import GoogleDrive

# Create GoogleDrive instance with authenticated GoogleAuth instance.
drive = GoogleDrive(gauth)
# Auto-iterate through all files that matches this query

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
	if file1['id'] == FILE_ID:
		#file1.GetContentFile(file1['title'], mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
		file1.GetContentFile('downloaded.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
		print("Downloaded file")


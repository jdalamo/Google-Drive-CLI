import os, io
import pickle
from sys import platform
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


if platform == 'win32':
	SLASH = '\\'
	DEFAULT_DOWNLOAD = ''
elif platform == 'darwin':
	SLASH = '/'
	DEFAULT_DOWNLOAD = ''
elif platform == 'linux':
	SLASH = '/'
	DEFAULT_DOWNLOAD = '/home/jd/Downloads'
else:
	SLASH = '/'
	DEFAULT_DOWNLOAD = '/'

# These files treated as folders so for now they're unsupported
EXCEPT_SET = {'numbers', 'pages', 'key'}

if os.path.exists('tracked_folders.json'):
	with open('tracked_folders.json', 'r') as f:
		tf_json = json.load(f)
		folders = tf_json['tracked_folders']

		googleDriveFolderIDs = [folders[folder]['drive_id'] for folder in folders]
		localFolderPaths = [folders[folder]['local_folder'] for folder in folders]
else:
	googleDriveFolderIDs = []
	localFolderPaths = []

# Authorize access and setup the Drive v3 API
SCOPES = ['https://www.googleapis.com/auth/drive']

pathToToken = os.path.join('config', 'token.pickle')
pathToCredentials = os.path.join('config', 'credentials.json')
creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists(pathToToken):
    with open(pathToToken, 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            pathToCredentials, SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open(pathToToken, 'wb') as token:
        pickle.dump(creds, token)

DRIVE = build('drive', 'v3', credentials=creds)
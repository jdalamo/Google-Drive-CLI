import os, io
from apiclient.http import MediaIoBaseDownload
import drivefile as df
from config.config import DRIVE, SLASH, EXCEPT_SET


def getFileID(wd, fileName):
	items = DRIVE.files().list(
		q="name = '{}' and '{}' in parents and trashed=false".format(fileName, wd.getDirIDs()[-1]),
		pageSize=1000, fields='files(id)').execute().get('files', [])

	return items[0]['id']


def getFileName(file_id):
	metadata = DRIVE.files().get(fileId=file_id, fields='name').execute()

	return metadata['name']


def searchChildrenByParent(parent_id):
	results = DRIVE.files().list(
		q="'{}' in parents and trashed=false and not fullText contains '.DS_Store'".format(parent_id),
		pageSize=1000, fields='nextPageToken, files(id, name, modifiedTime, mimeType, parents)').execute()
	items = results.get('files', [])

	return items


def listFiles(parent_id):
	results = DRIVE.files().list(
		q="'{}' in parents and trashed=false and not fullText contains '.DS_Store'".format(parent_id),
		pageSize=1000, fields='files(name)').execute()
	items = results.get('files', [])

	names = [i['name'] for i in items]
	
	return sorted(names)


def listFolders(parent_id):
	items = DRIVE.files().list(
		q="'{}' in parents and trashed=false and mimeType = 'application/vnd.google-apps.folder' and not fullText contains '.DS_Store'".format(parent_id),
		pageSize=1000, fields='files(name, mimeType)').execute().get('files', [])

	names = [i['name'] for i in items]
	
	return sorted(names)


# Automatically replaces file in destination
def downloadFile(file_id, filepath):
	request = DRIVE.files().get_media(fileId=file_id)
	fh = io.BytesIO()
	downloader = MediaIoBaseDownload(fh, request)
	done = False
	while done is False:
		status, done = downloader.next_chunk()
		print("Download %d%%." % int(status.progress() * 100))
		with io.open(filepath, 'wb') as f:
			fh.seek(0)
			f.write(fh.read())

def parseSpaceBackslashes(pieces):
	parsedParams = ' '.join(pieces)
	parsedParams = parsedParams.replace('\\', '')

	return parsedParams


# Calls searchChildrenByParent on the file id passed in.
# Then recursively looks through Google Drive file structure
# and adds DriveFile objects to lists based on if the item is a file or folder
# Look into turning this into a generator
def buildDriveFiles(file_id, filePath, fileList=[], folderList=[]):
	contents = searchChildrenByParent(file_id)

	# Can probably refactor this loop to handle .DS_Store files more elegantly
	for item in contents:
		newPath = filePath+SLASH+item['name']

		# Parent folder is returned as a list from API
		item['parents'] = item['parents'][0]

		if item['mimeType'][-6:] != 'folder' and item['name'] != '.DS_Store': # Can probably get rid of this ds_store check now
			fileList.append(df.DriveFile(item['id'], item['name'], item['parents'],
										 item['modifiedTime'], item['mimeType'], newPath))
		elif item['name'] == '.DS_Store':
			pass
		else:
			folderList.append(df.DriveFile(item['id'], item['name'], item['parents'],
										   item['modifiedTime'], item['mimeType'], newPath))
			buildDriveFiles(item['id'], newPath, fileList, folderList)

	return fileList, folderList


def localFileSearch(path, fileList=[], folderList=[]):
	contents = os.listdir(path)

	# Main processing of file tree
	for item in contents:
		if os.path.isdir(os.path.join(path, item)) and item[item.rfind('.')+1:] not in EXCEPT_SET:
			folderList.append(os.path.join(path, item))
			localFileSearch(os.path.join(path, item), fileList, folderList)
		elif not os.path.isdir(os.path.join(path, item)) and item != '.DS_Store':
			fileList.append(os.path.join(path, item))

	# Can maybe turn this into a tuple
	return fileList, folderList
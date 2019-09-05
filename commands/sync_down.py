import os
from config.config import googleDriveFolderIDs, localFolderPaths, DRIVE
import commands.common_functions as cf


def run():
	if len(googleDriveFolderIDs) == 0:
		print("No folders set to track Google Drive.  Add one with 'tf add' command.")
	else:
		for gdID, lf in zip(googleDriveFolderIDs, localFolderPaths):
			print(cf.getFileName(gdID) + ": ")
			driveFiles, driveFolders = cf.buildDriveFiles(gdID, lf)
			localFiles, localFolders = cf.localFileSearch(lf)
			for folder in driveFolders:
				if folder.get_filePath() not in localFolders:
					print("Creating folder {}".format(folder.get_filePath()))
					os.makedirs(folder.get_filePath())

			for file in driveFiles:
				if file.get_filePath() not in localFiles:
					print("Downloading file {}".format(file.get_fileName()), end=': ')
					cf.downloadFile(file.get_file_id(), file.get_filePath())

	print()
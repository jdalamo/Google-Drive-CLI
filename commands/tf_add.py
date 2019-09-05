from os import path
import json
import commands.common_functions as cf

def run(wd):
    _continue = False
    while not _continue:
        folderName = input("Enter the name of the Google Drive folder you want to track (must be in working directory): ")
        if folderName in cf.listFolders(wd.getDirIDs()[-1]):
            try:
                folderID = cf.getFileID(wd, folderName)
                _continue = True
            except Exception:
                print("Something went wrong, try re-entering the folder name")
        else:
            print("No such folder.  Make sure you are in the right directory")

    folderPath = ''
    while not path.exists(folderPath):
        folderPath = input("Enter in or paste the full path to the local folder you want to track Google Drive: ")
        if path.exists(folderPath):
            break
        print("That folder does not exist")

    if path.exists('tracked_folders.json'):
        with open('tracked_folders.json', 'r') as f:
            folders = json.load(f)

    else:
        folders = {
            'tracked_folders': {}
        }

    folders['tracked_folders'][folderName] = {
        'drive_id': folderID,
        'local_folder': folderPath
    }

    with open('tracked_folders.json', 'w') as f:
        json.dump(folders, f)

    print("Folder successfully added")

from os import path
import json
import commands.common_functions as cf

def run(params):
    folderName = cf.parseSpaceBackslashes(params)
    if path.exists('tracked_folders.json'):
        with open('tracked_folders.json', 'r') as f:
            folders = json.load(f)

        try:
            del folders['tracked_folders'][folderName]
            with open('tracked_folders.json', 'w') as f:
                json.dump(folders, f)
        except KeyError:
            print("Unrecognized folder: " + folderName)
            print("Folder not deleted")
        except Exception:
            print("Something happened, folder not deleted")

    else:
        print("No folders set to track Google Drive.  Add one with 'tf add' command.")
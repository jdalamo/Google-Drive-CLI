from os import path
import json
import commands.common_functions as cf

def run():
    with open('tracked_folders.json', 'r') as f:
        tf_json = json.load(f)

    folders = tf_json['tracked_folders']

    if bool(folders):
        for folder in folders:
            print("Google Drive folder '" + folder + "': ")
            print("Tracks local folder " + folders[folder]['local_folder'])
            print()
    else:
        print("No folders set to track Google Drive.  Add one with 'tf add' command.")
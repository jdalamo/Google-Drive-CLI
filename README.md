# A CLI for Google Drive written in Python

## About
---

Use this program to navigate Google Drive from within your terminal using the same Bash commands you'd use natively.
You can also download your files and set up folders to track Google Drive folders.

## Stack
---
Python

## Dependencies
---
- Google Drive API

## Commands
---
- pwd
    - Print the working directory
- ls
    - List the contents of the current working directory
- cd
    - Change into a new directory
- clear
    - Clear the terminal
- sync up
    - Push changes in local folder to tracked folder in Google Drive
- sync down
    - Pull changes in tracked Google Drive folder to local folder
- dl
    - Downloads specified file
- tf view
    - View tracked folders
- tf add
    - Add tracked folders
- tf del
    - Delete tracked folders
- help

## Get it running
---
1. Ensure you have Python 3 installed on your computer
2. Clone the directory
3. Go to https://developers.google.com/drive/api/v3/quickstart/python?authuser=1
4. Click "Enable the Drive API"
5. Click "Next" and then "Create"
6. Click "Download Client Configuration"
7. Copy the json file to Google-Drive-CLI/config (ensure it is named "credentials.json")
8. Run the following commands in the cloned directory:

Note: May need to use pip and python instead of pip3 and python3 if you don't have multiple versions of python installed
```
> pip3 install -r requirements.txt
> python3 cli.py
```
9. In the browser window that opened, select the account you want to use
10. Click "Advanced"
11. Click "Go to Google Drive CLI" (yours may say "Quickstart")
12. Click "Allow" twice
13. The program should now be running in your terminal
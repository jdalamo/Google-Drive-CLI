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
5. Go to https://console.developers.google.com/apis/dashboard and click "Credentials" on the left side menu
6. Click "Create Credentials" and then click "OAuth client ID"
7. Select "Other", name it whatever you like, and click "Create"
8. Click "Ok"
9. Click the credential you just created
10. Click "Download JSON"
11. Copy the json file to Google-Drive-CLI/config and rename it "credentials.json"
12. Run the following commands in the cloned directory:
```
> pip install -r requirements.txt
> python cli.py (may need to use 'python3 cli.py' if you have multiple versions of python installed)
```
13. In the browser window that opened, select the account you want to use
14. Click "Advanced"
15. Click "Go to Google Drive CLI" (yours may say "Quickstart")
16. Click "Allow" twice
17. The program should now be running in your terminal
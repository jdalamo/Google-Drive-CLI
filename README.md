# A CLI for Google Drive written in Python

Use this program to navigate Google Drive from within your terminal using the same Bash commands you'd use natively.
You can also download your files and set up folders to track Google Drive folders.

## Commands
---
- pwd
- ls
- cd
- sync up
    - Push changes in local folder to tracked folder in Google Drive
- sync down
    - Pull changes in tracked Google Drive folder to local folder
- dl
    - Downloads specified file
- help

## Get it running
---
1. Ensure you have Python 3 installed on your computer
2. Clone the directory
3. Go to https://developers.google.com/drive/api/v3/quickstart/python?authuser=1
4. Click "Enable the Drive API"
5. Click "Download Client Configuration" and copy the json file to Google-Drive-CLI/config
6. Run the following commands in the cloned directory:
```
> pip install -r requirements.txt
> python3 main.py
```
7. In the browser window that opened, select the account you want to use
8. Click "Advanced"
9. Click "Go to Google Drive CLI" (yours may say "Quickstart")
10. Click "Allow" twice
11. The program should now be running in your terminal
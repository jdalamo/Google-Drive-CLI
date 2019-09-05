from commands import helpDict

def run(params):
	param = ' '.join(params)
	if len(params) == 0:
		helpOutput = """
This is a command line interface for Google Drive. You can use the same bash commands you're used to in order navigate and view your files and folders. Run the help command followed by the name of another command to get more information on how to use it.
List of commands:
pwd
ls
cd
quit
sync up
sync down
dl
tf view
tf add
tf del
"""
		print(helpOutput)
	elif param in helpDict.helpText:
		print(helpDict.helpText[param])
	else:
		print("Unrecognized command: ", param)
import os, io
import drivefile as df
import workdir
from commands import _help, pwd, ls, cd, clear, sync_up, sync_down, dl, tf_view, tf_add, tf_del

def main():
	print("Google Drive CLI")
	print("Type 'help' for more information or 'quit' at anytime to quit the program.")
	workingDir = workdir.WorkDir()
	userInput = ''
	while userInput != 'quit':

		inputString = 'Drive:' + ('/'.join(workingDir.getDirNames())) + '$ '
		userInput = input(inputString)

		parentCommand = userInput.split(' ')[0]
		commandParams = userInput.split(' ')[1:]

		if parentCommand == 'help':
			_help.run(commandParams)
		elif parentCommand == 'pwd':
			pwd.run(workingDir)
		elif parentCommand == 'ls':
			ls.run(workingDir, commandParams)
		elif parentCommand == 'cd':
			cd.run(workingDir, commandParams)
		elif parentCommand == 'clear':
			clear.run()
		elif parentCommand == 'sync':
			if commandParams[0] == 'up':
				sync_up.run()
			elif commandParams[0] == 'down':
				sync_down.run()
			else:
				print("Unrecognized parameter to 'sync' command: " + commandParams[0])
		elif parentCommand == 'dl':
			dl.run(workingDir, commandParams)
		elif parentCommand == 'tf':
			if commandParams[0] == 'view':
				tf_view.run()
			elif commandParams[0] == 'add':
				tf_add.run(workingDir)
			elif commandParams[0] == 'del':
				tf_del.run(commandParams[1:])
			else:
				print("Unrecognized parameter to 'tf' command: " + commandParams[0])

		elif parentCommand != 'quit':
			print("Unrecognized command.  Type 'help' for help.")


if __name__ == '__main__':
	main()
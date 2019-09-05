import shutil
import commands.common_functions as cf

COLUMN_SPACE = 5

def run(wd, params):
	terminalWidth = shutil.get_terminal_size()[0]

	if len(params) == 0:
		fileNames = cf.listFiles(wd.getDirIDs()[-1])
	else:
		fileName = cf.parseSpaceBackslashes(params)
		fileID = cf.getFileID(wd, fileName)
		fileNames = cf.listFiles(fileID)
	try:
		longestName = sorted(fileNames, key=len, reverse=True)[0]
		numColumns = terminalWidth // (len(longestName) + COLUMN_SPACE)
		outputNameLists = [fileNames[i:i + numColumns] for i in range(0, len(fileNames), numColumns)]

		for nameList in outputNameLists:
			for name in nameList:
				formatString = '{:<' + str(len(longestName) + COLUMN_SPACE) + 's}'

				print(formatString.format(name), end='')
				if name == nameList[-1]:
					print()
		# print("\n")
	except IndexError:
		print('Empty directory')
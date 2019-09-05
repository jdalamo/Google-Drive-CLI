import commands.common_functions as cf

def run(wd, params):
	dirPath = parseParams(params)
	
	for entry in dirPath:
		if entry == '..' and len(wd.getDirNames()) == 1:
			print('In root directory')
		elif entry == '..':
			wd.removeDirName()
			wd.removeDirID()
		elif entry in cf.listFolders(wd.getDirIDs()[-1]):
			wd.addDirName(entry)
			wd.addDirID(cf.getFileID(wd, entry))
		else:
			print('No such file or directory--did you try to cd into a file?')

def parseParams(parameters):
	parsedParams = ' '.join(parameters)
	parsedParams = parsedParams.replace('\\', '')

	parsedParams = parsedParams.split('/')
	parsedParams = [p for p in parsedParams if p != ''] # Getting rid of extra '' in list when running 'cd ../'
	
	return parsedParams
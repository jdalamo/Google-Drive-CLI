class WorkDir:

    def __init__(self):
        self.__dirNames = ['root']
        self.__dirIDs = ['root']

    def getDirNames(self):
        return self.__dirNames

    def addDirName(self, name):
        self.__dirNames.append(name)

    def removeDirName(self):
        self.__dirNames.pop(-1)

    def getDirIDs(self):
        return self.__dirIDs

    def addDirID(self, id):
        self.__dirIDs.append(id)

    def removeDirID(self):
        self.__dirIDs.pop(-1)

import os
import commands.common_functions as cf
from config.config import DEFAULT_DOWNLOAD


def run(wd, params):
    fileName = cf.parseSpaceBackslashes(params)
    fileID = cf.getFileID(wd, fileName)
    filePath = os.path.join(DEFAULT_DOWNLOAD, fileName)
    try:
        cf.downloadFile(fileID, filePath)
    except Exception as err:
        print("Can only download files, not folders.\nError message:")
        print(err)
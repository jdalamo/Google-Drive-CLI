class DriveFile:

	def __init__(self, file_id, fileName, parent_id, RFCdateModified, mimeType, filePath):
		self.__file_id = file_id
		self.__fileName = fileName
		self.__parent_id = parent_id
		self.__RFCdateModified = RFCdateModified
		self.__mimeType = mimeType
		self.__filePath = filePath

	def get_file_id(self):
		return self.__file_id

	def get_fileName(self):
		return self.__fileName

	def get_parent_id(self):
		return self.__parent_id

	def get_RFCdateModified(self):
		return self.__RFCdateModified

	def get_mimeType(self):
		return self.__mimeType

	def get_filePath(self):
		return self.__filePath

from difflib import Differ


class Tkdiff:
	def __init__(self, firstFile, secondFile):
		self.__firstFile = firstFile
		self.__secondFile = secondFile

	def get__differ(self):
		return self.__d

	def resetDeffer(self):
		with open(self.__firstFile) as f:
		    file1_lines = f.readlines()
		with open(self.__secondFile) as f:
		    file2_lines = f.readlines()
		self.__d = Differ().compare(file1_lines, file2_lines)
	def filesDoesNotExist(self):
		try:
			with open(self.__firstFile) as f:
				file1_lines = f.readlines()
		except:
			raise ValueError("file " + str(self.__firstFile) + " does not exist")
			return True
		try:
			with open(self.__secondFile) as f:
				file2_lines = f.readlines()
		except:
			raise ValueError("file " + str(self.__secondFile) + " does not exist")
			return True
		return False

